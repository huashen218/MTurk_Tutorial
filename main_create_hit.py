import os
import json
from mturk_cores import MTurkManager, print_log
from frontend_cores import load_frontend_setting


def main():

    # ===============================
    # step1: Parsing Configurations
    # ===============================
    with open("./config.json", "r") as read_file:
        config = json.load(read_file)
    print_log("INFO", f" ====== Display Your Configuration ====== \n{config}")


    # ===============================
    # step2: MTurkManager Client Setup
    # ===============================
    """
    client functions to view:
    - client.get_account_balance()['AvailableBalance']
    - client.update_expiration_for_hit(
                HITId=hit_id,
                ExpireAt=datetime(2015, 1, 1),
            )
    - client.delete_hit(HITId=hit_id)
    - r = client.list_hits(MaxResults=100)
    - r = client.list_reviewable_hits(
        Status='Reviewable',
        MaxResults=max_results
        )
    - r = client.list_assignments_for_hit(
        HITId=hit_id,
        AssignmentStatuses=[status] if type(status) == str else status
    - r = client.get_assignment(AssignmentId=assignment_id)
    - r = client.approve_assignment(
            AssignmentId=assignment_id,
        )
    )
    """
    mturk_manager = MTurkManager(config)

    mturk_manager.set_environment()
    mturk_manager.setup_client()
    client = mturk_manager.client


    # ===============================
    # step3: MTurk Tasks  --- Create HIT
    # ===============================

    github_dir = "https://huashen218.github.io/images/"
    heroku_dir = "https://crowd-website.herokuapp.com/mturk_tweet/"
    for i in range(5):
        file_name = "c_change_tweet_t_" + str(i).zfill(6) + ".html"   # same with the file_name in frontend_cores.generate_htmls
        url = os.path.join(heroku_dir, file_name)
        frontend_setting = load_frontend_setting(url, height=800)
        response = mturk_manager.create_per_hit(frontend_setting)




if __name__ == '__main__':
    main()
