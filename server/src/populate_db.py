####################################################
####################################################
#                                                  #
# Note : Do not use this script for now            #
#                                                  #
####################################################
####################################################

if __name__ == '__main__':
    filepath = os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), 'env', 'credentials.txt'
    )
    username = ""
    password = ""
    with open(filepath) as file:
        lines = file.readlines()
        username = lines[0][:-1]
        password = lines[1][:-1]
