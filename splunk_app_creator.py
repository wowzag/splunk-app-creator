# importing os module
import os


def main():

    ## User defined attributes for the App
    print("\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Welcome to the Custom Splunk App Creator!")
    print("    I was created to make your life easier :-)")
    print("       Capabilities: 1 Custom App Creation       ")
    print("       Capabilities: Up to 8 log source stanzas  ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\n")
    print("Please adhere to the following naming convention:")
    print("Networking/FW Appliances:     <YourCompany_<Brand>_<Model>")
    print("Web/App Technology:     YourCompany_<OS>_<Technology><LogType>")
    print("\n")
    print("Examples:")
    print("Cisco Meraki Switch: Ex_Cisco_Meraki")
    print("Cisco Nexus Switch: Ex_Cisco_Nexus")
    print("\n")
    print("\n")
    print("Examples:")
    print("Apache - Ex_nix_Apache")
    print("strongDM Gateway Logs: Ex_nix_strongDMGwLogs")
    print("\n")
    print("-------------------------------------------------")
    print("\n")
    app_dir = input("Name of App: ")

    # Create directory for App, define Parent directory, and include a local
    directory = app_dir
    parent_dir = "<change me>"
    subdirectory ="local"

    # Path
    path = os.path.join(parent_dir, directory, subdirectory)

    # Create the directory
    os.makedirs(path)

    #User defined attributes for the inputs.conf file
    print("\n")
    print("\n")
    print("Next, please define what log file we will ingest.")
    print("Be sure to include exact path, wildcards are allowed, i.e - /data/log/ciscomeraki*")
    print("\n")
    print("\n")
    log_source = input("Path of log file: ")
    print("\n")
    print("\n")
    print("Choose an index, ex: fw, networkevents, webevents, appevents \n")
    log_index = input("What index will this data go to?: ")
    print("\n")
    print("\n")
    print("Next, please define what sourcetype this file will use. This is important, please be sure to define the correct sourcetype. ex: apache:access, pan:threat")
    log_sourcetype = input("Sourcetype:")
    print("\n")
    print("\n")
    print("You entered: path of log file = " + log_source + ", index = " + log_index + ", sourcetype = " + log_sourcetype)
    typo_check = input("Is the spelling and syntax correct? type [yes] or [no]:    ")
    if typo_check == 'no':
        print("Something is wrong with your spelling, please re-run program!")
        exit()

    #Create inputs.conf
    inputs_directory = path
    filename = "inputs.conf"
    file_path = os.path.join(inputs_directory, filename)
    f= open(file_path,"w+")
    f.write("[monitor://" + log_source + "]" + "\n")
    f.write("sourcetype="+ log_sourcetype + "\n")
    f.write("disabled=0\n")
    f.write("index="+ log_index + "\n")
    f.write("_TCP_ROUTING=splunkcloud\n")
    f.close()

    question = input("Do you have any more stanzas to add?: type [yes] or [no]:     ")
    if question == 'no':
        # Print inputs.conf
        with open(file_path, "r+") as inputs_file:
        # Reading from a file
            print("Congrats, your app is complete!")
            print("\n")
            print("Your newly created inputs.conf contains the following:")
            print("\n")
            print("\n")
            print(inputs_file.read())

        print("Directory '% s' created" % directory)
        print("Subdirectory '% s' created" % subdirectory)
        print("File '% s' created" % filename)

        print("\n")
        print("Next steps:\n")
        print("     1. Navigate to <change me dir> in WinSCP. \n")
        print("     2. Copy the newly created Splunk App \n")
        print("     3. Open Sourcetree \n")
        print("     4. Use 'deployment-server-splunk' repo \n")
        print("     5. Navigate to \opt\splunk\etc\deployment-apps \n")
        print("     6. Paste app \n")
        print("     7. Stage, comment, commit, push. \n")
        exit()

    else:
        #User defined attributes for the inputs.conf file
        print("\n")
        print("\n")
        print("Next, please define what log file we will ingest.")
        print("Be sure to include exact path, wildcards are allowed, i.e - /data/log/ciscomeraki*")
        print("\n")
        print("\n")
        log_source2 = input("Path of log file: ")
        print("\n")
        print("\n")
        print("Choose an index, ex: fw, networkevents, webevents, appevents \n")
        log_index2 = input("What index will this data go to?: ")
        print("\n")
        print("\n")
        print("Next, please define what sourcetype this file will use. This is important, please be sure to define the correct sourcetype. ex: apache:access, pan:threat")
        log_sourcetype2 = input("Sourcetype of log: ")

        print("\n")
        print("\n")
        print("You entered: path of log file = " + log_source2 + ", index = " + log_index2 + ", sourcetype = " + log_sourcetype2)
        typo_check = input("Is the spelling and syntax correct? type [yes] or [no]:    ")
        if typo_check == 'no':
            print("Something is wrong with your spelling, please re-run program!")
            exit()
        f= open(file_path,"a")
        f.write("\n")
        f.write("[monitor://" + log_source2 + "]" + "\n")
        f.write("sourcetype="+ log_sourcetype2 + "\n")
        f.write("disabled=0\n")
        f.write("index="+ log_index2 + "\n")
        f.write("_TCP_ROUTING=splunkcloud\n")
        f.close()
        question = input("Do you have any more stanzas to add?: type [yes] or [no]:     ")
        if question == 'no':
            # Print inputs.conf
            with open(file_path, "r+") as inputs_file:
            # Reading from a file
                print("Congrats, your app is complete!")
                print("\n")
                print("Your newly created inputs.conf contains the following:")
                print("\n")
                print("\n")
                print(inputs_file.read())

            print("Directory '% s' created" % directory)
            print("Subdirectory '% s' created" % subdirectory)
            print("File '% s' created" % filename)

            print("\n")
            print("Next steps:\n")
            print("     1. Navigate to /home/mcs_automation/Splunk/ in WinSCP. \n")
            print("     2. Copy the newly created Splunk App \n")
            print("     3. Open Sourcetree \n")
            print("     4. Use 'deployment-server-splunk' repo \n")
            print("     5. Navigate to \opt\splunk\etc\deployment-apps \n")
            print("     6. Paste app \n")
            print("     7. Stage, comment, commit, push. \n")
            exit()
        else:
            #User defined attributes for the inputs.conf file
            print("\n")
            print("\n")
            print("Next, please define what log file we will ingest.")
            print("Be sure to include exact path, wildcards are allowed, i.e - /data/log/ciscomeraki*")
            print("\n")
            print("\n")
            log_source3 = input("Path of log file: ")
            print("\n")
            print("\n")
            print("Choose an index, ex: fw, networkevents, webevents, appevents \n")
            log_index3 = input("What index will this data go to?: ")
            print("\n")
            print("\n")
            print("Next, please define what sourcetype this file will use. This is important, please be sure to define the correct sourcetype. ex: apache:access, pan:threat")
            log_sourcetype3 = input("Sourcetype of log: ")

            print("\n")
            print("\n")
            print("You entered: path of log file = " + log_source3 + ", index = " + log_index3 + ", sourcetype = " + log_sourcetype3)
            typo_check = input("Is the spelling and syntax correct? type [yes] or [no]:    ")
            if typo_check == 'no':
                print("Something is wrong with your spelling, please re-run program!")
                exit()
            f= open(file_path,"a")
            f.write("\n")
            f.write("[monitor://" + log_source3 + "]" + "\n")
            f.write("sourcetype="+ log_sourcetype3 + "\n")
            f.write("disabled=0\n")
            f.write("index="+ log_index3 + "\n")
            f.write("_TCP_ROUTING=splunkcloud\n")
            f.close()
            question = input("Do you have any more stanzas to add?: type [yes] or [no]:     ")
            if question == 'no':
                # Print inputs.conf
                with open(file_path, "r+") as inputs_file:
                # Reading from a file
                    print("Congrats, your app is complete!")
                    print("\n")
                    print("Your newly created inputs.conf contains the following:")
                    print("\n")
                    print("\n")
                    print(inputs_file.read())

                print("Directory '% s' created" % directory)
                print("Subdirectory '% s' created" % subdirectory)
                print("File '% s' created" % filename)

                print("\n")
                print("Next steps:\n")
                print("     1. Navigate to /home/mcs_automation/Splunk/ in WinSCP. \n")
                print("     2. Copy the newly created Splunk App \n")
                print("     3. Open Sourcetree \n")
                print("     4. Use 'deployment-server-splunk' repo \n")
                print("     5. Navigate to \opt\splunk\etc\deployment-apps \n")
                print("     6. Paste app \n")
                print("     7. Stage, comment, commit, push. \n")
                exit()
            else:
                #User defined attributes for the inputs.conf file
                print("\n")
                print("\n")
                print("Next, please define what log file we will ingest.")
                print("Be sure to include exact path, wildcards are allowed, i.e - /data/log/ciscomeraki*")
                print("\n")
                print("\n")
                log_source4 = input("Path of log file: ")
                print("\n")
                print("\n")
                print("Choose an index, ex: fw, networkevents, webevents, appevents \n")
                log_index4 = input("What index will this data go to?: ")
                print("\n")
                print("\n")
                print("Next, please define what sourcetype this file will use. This is important, please be sure to define the correct sourcetype. ex: apache:access, pan:threat")
                log_sourcetype4 = input("Sourcetype of log: ")

                print("\n")
                print("\n")
                print("You entered: path of log file = " + log_source4 + ", index = " + log_index4 + ", sourcetype = " + log_sourcetype4)
                typo_check = input("Is the spelling and syntax correct? type [yes] or [no]:    ")
                if typo_check == 'no':
                    print("Something is wrong with your spelling, please re-run program!")
                    exit()
                f= open(file_path,"a")
                f.write("\n")
                f.write("[monitor://" + log_source4 + "]" + "\n")
                f.write("sourcetype="+ log_sourcetype4 + "\n")
                f.write("disabled=0\n")
                f.write("index="+ log_index4 + "\n")
                f.write("_TCP_ROUTING=splunkcloud\n")
                f.close()
                question = input("Do you have any more stanzas to add?: type [yes] or [no]:     ")
                if question == 'no':
                    # Print inputs.conf
                    with open(file_path, "r+") as inputs_file:
                    # Reading from a file
                        print("Congrats, your app is complete!")
                        print("\n")
                        print("Your newly created inputs.conf contains the following:")
                        print("\n")
                        print("\n")
                        print(inputs_file.read())

                    print("Directory '% s' created" % directory)
                    print("Subdirectory '% s' created" % subdirectory)
                    print("File '% s' created" % filename)

                    print("\n")
                    print("Next steps:\n")
                    print("     1. Navigate to /home/mcs_automation/Splunk/ in WinSCP. \n")
                    print("     2. Copy the newly created Splunk App \n")
                    print("     3. Open Sourcetree \n")
                    print("     4. Use 'deployment-server-splunk' repo \n")
                    print("     5. Navigate to \opt\splunk\etc\deployment-apps \n")
                    print("     6. Paste app \n")
                    print("     7. Stage, comment, commit, push. \n")
                    exit()
                else:
                    #User defined attributes for the inputs.conf file
                    print("\n")
                    print("\n")
                    print("Next, please define what log file we will ingest.")
                    print("Be sure to include exact path, wildcards are allowed, i.e - /data/log/ciscomeraki*")
                    print("\n")
                    print("\n")
                    log_source5 = input("Path of log file: ")
                    print("\n")
                    print("\n")
                    print("Choose an index, ex: fw, networkevents, webevents, appevents \n")
                    log_index5 = input("What index will this data go to?: ")
                    print("\n")
                    print("\n")
                    print("Next, please define what sourcetype this file will use. This is important, please be sure to define the correct sourcetype. ex: apache:access, pan:threat")
                    log_sourcetype5 = input("Sourcetype of log: ")

                    print("\n")
                    print("\n")
                    print("You entered: path of log file = " + log_source5 + ", index = " + log_index5 + ", sourcetype = " + log_sourcetype5)
                    typo_check = input("Is the spelling and syntax correct? type [yes] or [no]:    ")
                    if typo_check == 'no':
                        print("Something is wrong with your spelling, please re-run program!")
                        exit()
                    f= open(file_path,"a")
                    f.write("\n")
                    f.write("[monitor://" + log_source5 + "]" + "\n")
                    f.write("sourcetype="+ log_sourcetype5 + "\n")
                    f.write("disabled=0\n")
                    f.write("index="+ log_index5 + "\n")
                    f.write("_TCP_ROUTING=splunkcloud\n")
                    f.close()
                    question = input("Do you have any more stanzas to add?: type [yes] or [no]:       ")
                    if question == 'no':
                        # Print inputs.conf
                        with open(file_path, "r+") as inputs_file:
                        # Reading from a file
                            print("Congrats, your app is complete!")
                            print("\n")
                            print("Your newly created inputs.conf contains the following:")
                            print("\n")
                            print("\n")
                            print(inputs_file.read())

                        print("Directory '% s' created" % directory)
                        print("Subdirectory '% s' created" % subdirectory)
                        print("File '% s' created" % filename)

                        print("\n")
                        print("Next steps:\n")
                        print("     1. Navigate to /home/mcs_automation/Splunk/ in WinSCP. \n")
                        print("     2. Copy the newly created Splunk App \n")
                        print("     3. Open Sourcetree \n")
                        print("     4. Use 'deployment-server-splunk' repo \n")
                        print("     5. Navigate to \opt\splunk\etc\deployment-apps \n")
                        print("     6. Paste app \n")
                        print("     7. Stage, comment, commit, push. \n")
                        exit()
                    else:
                        #User defined attributes for the inputs.conf file
                        print("\n")
                        print("\n")
                        print("Next, please define what log file we will ingest.")
                        print("Be sure to include exact path, wildcards are allowed, i.e - /data/log/ciscomeraki*")
                        print("\n")
                        print("\n")
                        log_source6 = input("Path of log file: ")
                        print("\n")
                        print("\n")
                        print("Choose an index, ex: fw, networkevents, webevents, appevents \n")
                        log_index6 = input("What index will this data go to?: ")
                        print("\n")
                        print("\n")
                        print("Next, please define what sourcetype this file will use. This is important, please be sure to define the correct sourcetype. ex: apache:access, pan:threat")
                        log_sourcetype6 = input("Sourcetype of log: ")

                        print("\n")
                        print("\n")
                        print("You entered: path of log file = " + log_source6 + ", index = " + log_index6 + ", sourcetype = " + log_sourcetype6)
                        typo_check = input("Is the spelling and syntax correct? type [yes] or [no]:    ")
                        if typo_check == 'no':
                            print("Something is wrong with your spelling, please re-run program!")
                            exit()
                        f= open(file_path,"a")
                        f.write("\n")
                        f.write("[monitor://" + log_source6 + "]" + "\n")
                        f.write("sourcetype="+ log_sourcetype6 + "\n")
                        f.write("disabled=0\n")
                        f.write("index="+ log_index6 + "\n")
                        f.write("_TCP_ROUTING=splunkcloud\n")
                        f.close()
                        question = input("Do you have any more stanzas to add?: type [yes] or [no]:     ")
                        if question == 'no':
                            # Print inputs.conf
                            with open(file_path, "r+") as inputs_file:
                            # Reading from a file
                                print("Congrats, your app is complete!")
                                print("\n")
                                print("Your newly created inputs.conf contains the following:")
                                print("\n")
                                print("\n")
                                print(inputs_file.read())

                            print("Directory '% s' created" % directory)
                            print("Subdirectory '% s' created" % subdirectory)
                            print("File '% s' created" % filename)

                            print("\n")
                            print("Next steps:\n")
                            print("     1. Navigate to /home/mcs_automation/Splunk/ in WinSCP. \n")
                            print("     2. Copy the newly created Splunk App \n")
                            print("     3. Open Sourcetree \n")
                            print("     4. Use 'deployment-server-splunk' repo \n")
                            print("     5. Navigate to \opt\splunk\etc\deployment-apps \n")
                            print("     6. Paste app \n")
                            print("     7. Stage, comment, commit, push. \n")
                            exit()
                        else:
                            #User defined attributes for the inputs.conf file
                            print("\n")
                            print("\n")
                            print("Next, please define what log file we will ingest.")
                            print("Be sure to include exact path, wildcards are allowed, i.e - /data/log/ciscomeraki*")
                            print("\n")
                            print("\n")
                            log_source7 = input("Path of log file: ")
                            print("\n")
                            print("\n")
                            print("Choose an index, ex: fw, networkevents, webevents, appevents \n")
                            log_index7 = input("What index will this data go to?: ")
                            print("\n")
                            print("\n")
                            print("Next, please define what sourcetype this file will use. This is important, please be sure to define the correct sourcetype. ex: apache:access, pan:threat")
                            log_sourcetype7 = input("Sourcetype of log: ")

                            print("\n")
                            print("\n")
                            print("You entered: path of log file = " + log_source7 + ", index = " + log_index7 + ", sourcetype = " + log_sourcetype7)
                            typo_check = input("Is the spelling and syntax correct? type [yes] or [no]:    ")
                            if typo_check == 'no':
                                print("Something is wrong with your spelling, please re-run program!")
                                exit()
                            f= open(file_path,"a")
                            f.write("\n")
                            f.write("[monitor://" + log_source7 + "]" + "\n")
                            f.write("sourcetype="+ log_sourcetype7 + "\n")
                            f.write("disabled=0\n")
                            f.write("index="+ log_index7 + "\n")
                            f.write("_TCP_ROUTING=splunkcloud\n")
                            f.close()
                            question = input("Do you have any more stanzas to add?: type [yes] or [no]:     ")
                            if question == 'no':
                                # Print inputs.conf
                                with open(file_path, "r+") as inputs_file:
                                # Reading from a file
                                    print("Congrats, your app is complete!")
                                    print("\n")
                                    print("Your newly created inputs.conf contains the following:")
                                    print("\n")
                                    print("\n")
                                    print(inputs_file.read())

                                print("Directory '% s' created" % directory)
                                print("Subdirectory '% s' created" % subdirectory)
                                print("File '% s' created" % filename)

                                print("\n")
                                print("Next steps:\n")
                                print("     1. Navigate to /home/mcs_automation/Splunk/ in WinSCP. \n")
                                print("     2. Copy the newly created Splunk App \n")
                                print("     3. Open Sourcetree \n")
                                print("     4. Use 'deployment-server-splunk' repo \n")
                                print("     5. Navigate to \opt\splunk\etc\deployment-apps \n")
                                print("     6. Paste app \n")
                                print("     7. Stage, comment, commit, push. \n")
                                exit()
                            else:
                                #User defined attributes for the inputs.conf file
                                print("\n")
                                print("\n")
                                print("Next, please define what log file we will ingest.")
                                print("Be sure to include exact path, wildcards are allowed, i.e - /data/log/ciscomeraki*")
                                print("\n")
                                print("\n")
                                log_source8 = input("Path of log file: ")
                                print("\n")
                                print("\n")
                                print("Choose an index, ex: fw, networkevents, webevents, appevents \n")
                                log_index8 = input("What index will this data go to?: ")
                                print("\n")
                                print("\n")
                                print("Next, please define what sourcetype this file will use. This is important, please be sure to define the correct sourcetype. ex: apache:access, pan:threat")
                                log_sourcetype8 = input("Sourcetype of log: ")

                                print("\n")
                                print("\n")
                                print("You entered: path of log file = " + log_source8 + ", index = " + log_index8 + ", sourcetype = " + log_sourcetype8)
                                typo_check = input("Is the spelling and syntax correct? type [yes] or [no]:    :  ")
                                if typo_check == 'no':
                                    print("Something is wrong with your spelling, please re-run program!")
                                    exit()
                                f= open(file_path,"a")
                                f.write("\n")
                                f.write("[monitor://" + log_source8 + "]" + "\n")
                                f.write("sourcetype="+ log_sourcetype8 + "\n")
                                f.write("disabled=0\n")
                                f.write("index="+ log_index8 + "\n")
                                f.write("_TCP_ROUTING=splunkcloud\n")
                                f.close()
                                print("I have reached the end of my Pythonic life.")
                                with open(file_path, "r+") as inputs_file:
                                    # Reading from a file
                                    print("Congrats, your app is complete!")
                                    print("\n")
                                    print("Your newly created inputs.conf contains the following:")
                                    print("\n")
                                    print("\n")
                                    print(inputs_file.read())

                                print("Directory '% s' created" % directory)
                                print("Subdirectory '% s' created" % subdirectory)
                                print("File '% s' created" % filename)

                                print("\n")
                                print("Next steps:\n")
                                print("     1. Navigate to /home/mcs_automation/Splunk/ in WinSCP. \n")
                                print("     2. Copy the newly created Splunk App \n")
                                print("     3. Open Sourcetree \n")
                                print("     4. Use 'deployment-server-splunk' repo \n")
                                print("     5. Navigate to \opt\splunk\etc\deployment-apps \n")
                                print("     6. Paste app \n")
                                print("     7. Stage, comment, commit, push. \n")
                            exit()
if __name__== "__main__":
  main()
