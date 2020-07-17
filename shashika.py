            print(bar)
            print("\n\033[1;32;40m [+] ඩේටා නෑ පොන්න ශෂිකයෝ ඊලඟ එක බලපන් ... [+]")
            print(bar)
        elif resp == '<Response [200]>':
            print(bar)
            print("\n\033[1;32;40m [+] ඩේටා ආවා පොන්න ශෂිකයෝ ... [+]")
            print(bar)
        else:
            print(bar)
            print("\n\033[1;31;40m [+] සිග්නල් නෑ ශෂික පොන්නයෝ ... [+]")
            print(bar)

        ss+=1
        print("\033[1;0;40m\n",str(ss), "ඊලඟ Request එක එනකන් තත්පර 100ක් ඉඳපන් පොන්න ශෂිකයෝ",end="")
        for i in range(180):

            pr = i/180*100
            print("\033[1;36;40m\n>>> [+]",str(int(pr)) +"% ",end="")

            time.sleep(0.5)
            sys.stdout.write("\033[F")

    os.system('figlet FINISHED')
    again()


def again():
    again = input('\033[1;0;40m\nDo You want use again (y/n) - ')
    if again == "y" or again == "Y":
        main()
    elif again == "n" or again == "N":
        quit()
    else:
        print('\033[1;31;40mEnter valid letter')
        again()


if __name__ == "__main__":
    main()
