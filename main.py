# ______     __    __     ______     __     __            __  __     __  __     __   __     ______   ______     ______    
#/\  ___\   /\ "-./  \   /\  __ \   /\ \   /\ \          /\ \_\ \   /\ \/\ \   /\ "-.\ \   /\__  _\ /\  ___\   /\  == \   
#\ \  __\   \ \ \-./\ \  \ \  __ \  \ \ \  \ \ \____     \ \  __ \  \ \ \_\ \  \ \ \-.  \  \/_/\ \/ \ \  __\   \ \  __<   
# \ \_____\  \ \_\ \ \_\  \ \_\ \_\  \ \_\  \ \_____\     \ \_\ \_\  \ \_____\  \ \_\\"\_\    \ \_\  \ \_____\  \ \_\ \_\ 
#  \/_____/   \/_/  \/_/   \/_/\/_/   \/_/   \/_____/      \/_/\/_/   \/_____/   \/_/ \/_/     \/_/   \/_____/   \/_/ /_/ 

import emailhunter

# Declare empty list to hold dictionaries of configured emails
configured_emails = []

if __name__ == "__main__":
    for monitored_email in monitored_emails:
        check_first_run(monitored_email)
