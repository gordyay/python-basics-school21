import sys


def lists_to_set():
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
               'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
               'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
                    'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
                    'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

    if (len(sys.argv) == 2):
        clients_set = set(clients)
        participants_set = set(participants)
        recipients_set = set(recipients)
        if sys.argv[1] == "call_center":
            print(list(clients_set-recipients_set))
        elif sys.argv[1] == "potential_clients":
            print(list(participants_set-clients_set))
        elif sys.argv[1] == "loyalty_program":
            print(list(clients_set - participants_set))
        else:
            print("wrong name of argument\nselect one of these commands\ncall_center || potential_clients || loyalty_program")
    else:
        print("There can only be one argument here")


if __name__ == '__main__':
    lists_to_set()
