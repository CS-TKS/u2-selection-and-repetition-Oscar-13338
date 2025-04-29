print("Welcome to the SDG Information and Mini Quiz Program!")

SDG_list = ['No Poverty', 'Zero Hunger', 'Good Health and Well-being', 'Quality Education', 'Gender Equality', 'Clean Water and Sanitation', 'Affordable and Clean Energy', 'Decent Work and Economic Growth', 'Industry, Innovation and Infrastructure', 'Reduced Inequality', 'Sustainable Cities and Communities', 'Responsible Consumption and Production', 'Climate Action', 'Life Below Water', 'Life on Land', 'Peace, Justice and Strong Institutions', 'Partnerships for the Goals']

print("Here are the SDG goals you can choose from:")
for goal in SDG_list:
    print(goal)

valid_input = False
while not valid_input:
    SDG_choice = input("Enter your SDG goal of choice (example: Quality Education): ").lower()

    if SDG_choice == 'no poverty':
        print(SDG_list[0])
        print("The goal is to end poverty in all its forms everywhere.")
        answer = input(" Does SDG 1 aim to end poverty in all forms? (Yes / No): ").lower()
        if answer == "yes":
            print("Correct answer!")
        else:
            print("Wrong answer")
        valid_input = True

    elif SDG_choice == 'zero hunger':
        print(SDG_list[1])
        print("This goal aims to end hunger, achieve food security and improved nutrition, and promote sustainable agriculture.")
        answer = input(" Does SDG 2 aim to end hunger through sustainable agriculture? (Yes / No): ").lower()
        if answer == "yes":
            print("Correct answer!")
        else:
            print("Wrong answer")
        valid_input = True

    elif SDG_choice == 'good health and well-being':
        print(SDG_list[2])
        print("This goal aims to ensure healthy lives and promote well-being for all at all ages.")
        answer = input(" Does SDG 3 focus on mental health as well as physical health? (Yes / No): ").lower()
        if answer == "yes":
            print("Correct answer!")
        else:
            print("Wrong answer")
        valid_input = True

    elif SDG_choice == 'quality education':
        print(SDG_list[3])
        print("This goal aims to ensure inclusive and equitable quality education and promote lifelong learning opportunities for all.")
        answer = input(" Does SDG 4 aim to ensure education only for adults? (Yes / No): ").lower()
        if answer == "no":
            print("Correct answer!")
        else:
            print("Wrong answer")

        valid_input = True

    elif SDG_choice == 'gender equality':
        print(SDG_list[4])
        print("This goal aims to achieve gender equality and empower all women and girls.")
        answer = input(" Does SDG 5 focus on empowering men and boys? (Yes / No): ").lower()
        if answer == "no":
            print("Correct answer!")
        else:
            print("Wrong answer")

        valid_input = True

    elif SDG_choice == 'clean water and sanitation':
        print(SDG_list[5])
        print("This goal aims to ensure availability and sustainable management of water and sanitation for all.")
        answer = input(" Is access to clean water a major focus of SDG 6? (Yes / No): ").lower()
        if answer == "yes":
            print("Correct answer!")
        else:
            print("Wrong answer")

        valid_input = True

    elif SDG_choice == 'affordable and clean energy':
        print(SDG_list[6])
        print("SDG 7 ensures access to affordable, reliable, sustainable, and modern energy for all.")
        answer = input(" Does SDG 7 aim to promote fossil fuels? (Yes / No): ").lower()
        if answer == "no":
            print("Correct answer!")
        else:
            print("Wrong answer")

        valid_input = True

    elif SDG_choice == 'decent work and economic growth':
        print(SDG_list[7])
        print("SDG 8 promotes sustained, inclusive, and sustainable economic growth, full and productive employment, and decent work for all.")
        answer = input(" Does SDG 8 promote both economic growth and decent work for all? (Yes / No): ").lower()
        if answer == "yes":
            print("Correct answer!")
        else:
            print("Wrong answer")

        valid_input = True

    elif SDG_choice == 'industry, innovation and infrastructure':
        print(SDG_list[8])
        print(
            "SDG 9 builds resilient infrastructure, promotes inclusive and sustainable industrialization, and fosters innovation.")
        answer = input(" Does SDG 9 aim to eliminate all industries worldwide? (Yes / No): ").lower()
        if answer == "no":
            print("Correct answer!")
        else:
            print("Wrong answer")

        valid_input = True

    elif SDG_choice == 'reduced inequality':
        print(SDG_list[9])
        print("SDG 10 aims to reduce inequality within and among countries.")
        answer = input(" Does SDG 10 focus on reducing inequality between developed and developing countries? (Yes / No): ").lower()
        if answer == "yes":
            print("Correct answer!")
        else:
            print("Wrong answer")

        valid_input = True

    elif SDG_choice == 'sustainable cities and communities':
        print(SDG_list[10])
        print("SDG 11 aims to make cities and human settlements inclusive, safe, resilient, and sustainable.")
        answer = input(" Does SDG 11 focus on making cities bigger and more crowded? (Yes / No): ").lower()
        if answer == "no":
            print("Correct answer!")
        else:
            print("Wrong answer")

        valid_input = True

    elif SDG_choice == 'responsible consumption and production':
        print(SDG_list[11])
        print(" SDG 12 focuses on ensuring sustainable consumption and production patterns.")
        answer = input(" Does SDG 12 aim to reduce waste and encourage sustainable practices? (Yes / No): ").lower()
        if answer == "yes":
            print("Correct answer!")
        else:
            print("Wrong answer")

        valid_input = True

    elif SDG_choice == 'climate action':
        print(SDG_list[12])
        print(" SDG 13 focuses on taking urgent action to combat climate change and its impacts. ")
        answer = input(" Does SDG 13 focus only on reducing carbon emissions? (Yes / No): ").lower()
        if answer == "no":
            print("Correct answer!")
        else:
            print("Wrong answer")

        valid_input = True

    elif SDG_choice == 'life below water':
        print(SDG_list[13])
        print(" SDG 14 aims to conserve and sustainably use the oceans, seas, and marine resources for sustainable development. ")
        answer = input(" Does SDG 14 aim to protect marine ecosystems? (Yes / No): ").lower()
        if answer == "yes":
            print("Correct answer!")
        else:
            print("Wrong answer")

        valid_input = True

    elif SDG_choice == 'life on land':
        print(SDG_list[14])
        print(" SDG 15 focuses on protecting, restoring, and promoting the sustainable use of terrestrial ecosystems. ")
        answer = input(" Does SDG 15 focus on both land and ocean ecosystems? (Yes / No): ").lower()
        if answer == "yes":
            print("Correct answer!")
        else:
            print("Wrong answer")

        valid_input = True

    elif SDG_choice == 'peace, justice and strong institutions':
        print(SDG_list[15])
        print(" SDG 16 promotes peaceful and inclusive societies for sustainable development, provides access to justice for all, and builds effective, accountable institutions at all levels. ")
        answer = input(" Does SDG 16 aim to promote peace and justice? (Yes / No): ").lower()
        if answer == "yes":
            print("Correct answer!")
        else:
            print("Wrong answer")

        valid_input = True

    elif SDG_choice == 'partnerships for the goals':
        print(SDG_list[16])
        print(" SDG 17 focuses on strengthening the means of implementation and revitalizing the global partnership for sustainable development. ")
        answer = input(" Does SDG 17 focus on building partnerships for achieving the SDGs? (Yes / No): ").lower()
        if answer == "yes":
            print("Correct answer!")
        else:
            print("Wrong answer")

        valid_input = True

print("Thank you for completing my SDG quiz!")
exit()

