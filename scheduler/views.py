from concurrent import futures
import json
import time

from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from test_utils.models import TestCase
from farm.models import Board
from threading import Lock


# Create your views here.
@csrf_exempt
def schedule_job(request):
    data = {}

    if request.method == "POST":
        test_jira_id_list = eval(request.POST.get("test_jira_id_list", "[]"))
        capability = request.POST.get("capability", "no-board")

        # fetch and assign test cases to job
        # test_cases
        test_case_obj_list = []
        for jira_id in test_jira_id_list:
            try:
                test_case_obj = TestCase.objects.get(jira_id=jira_id)
                test_case_obj_list.append(test_case_obj)
            except Exception as e:
                print("[ Error ] TestCase Not found.", e)

        # fetch boards and assign the test cases
        filter_object = Q()
        for cap in capability.split('_'):
            filter_object &= Q(capability__icontains=cap)
        boards = Board.objects.filter(filter_object)
        boards_count = len(boards)

        # schedule the test on board
        # We can use a with statement to ensure threads are cleaned up promptly
        with futures.ThreadPoolExecutor(max_workers=boards_count) as executor:
            # start the tasks
            mutex = Lock()
            function_ptr = {executor.submit(run_test, mutex, boards, test_case): test_case for test_case in
                            test_case_obj_list}

            # save the results
            for future in futures.as_completed(function_ptr):
                try:
                    result_data = future.result()
                    board_name = str(result_data['board_obj'].name)
                    jira_test_id = str(result_data['test_case_obj'].jira_id)

                    if board_name not in data:
                        data[board_name] = []
                    data[board_name].append(jira_test_id)
                    print(jira_test_id, "is done.")
                except Exception as exc:
                    print('generated an exception:', exc)

    return JsonResponse(data)


def run_test(mutex, board_pool, test_obj):
    # fetch the free board
    free_board = None
    while free_board is None:
        try:
            with mutex:
                # Reserve the board
                free_board = board_pool.filter(is_free=True)[0]
                free_board.is_free = False
                free_board.save()
        except:
            time.sleep(1)

    request_json = json.loads(test_obj.request_json)
    jira_id = test_obj.jira_id

    # Execute the jira test flow
    print(f"[ {jira_id} on {free_board.name}] : {request_json['name']}")
    for block in request_json["test_flow"]:
        if block["command"] == "print":
            print(f"[ {jira_id} on {free_board.name}] : {block["msg"]}")
        else:
            time.sleep(block["duration"])

    # release the board
    free_board.is_free = True
    free_board.save()
    return {
        "board_obj": free_board,
        "test_case_obj": test_obj,
    }
