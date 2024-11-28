import sys
import os.path

"""
LAUNCH FORMAT:
- python3 [this python file] [log file] [client | resource]
"""


class Logger:

    # Method for get most activity user
    @staticmethod
    def get_most_activity_user(file:str) -> str:
        activity_users = {}
        with open(file, 'r') as file:
            while True:
                text = file.readline()
                if not text:
                    return max(activity_users, key=activity_users.get)
                # Поиск активного
                user_ip = text.split(" ")[0]
                if user_ip not in activity_users:
                    activity_users[user_ip] = 1
                else:
                    activity_users[user_ip] += 1

    # Method for get popular resource
    @staticmethod
    def get_popular_resource(file:str) -> str:
        popular_resource = {}
        with open(file, 'r') as file:
            while True:
                text = file.readline()
                if not text:
                    return max(popular_resource, key=popular_resource.get)

                resource = text.split('"')[-2]
                if resource not in popular_resource:
                    popular_resource[resource] = 1
                else:
                    popular_resource[resource] += 1

if __name__ == '__main__':
    argv = sys.argv[1::]
    read_file = argv[0]
    log_filters = argv[1:3]

    if not os.path.exists(read_file):
        sys.exit("File not found")

    logger = Logger()
    for log_filter in log_filters:
        if log_filter.lower() == "client":
            print("Most active client: " + logger.get_most_activity_user(read_file))
        elif log_filter.lower() == "resource":
            print("Most popular resource: " + logger.get_popular_resource(read_file))
        else:
            print("Method \"" + log_filter + "\" not supported")