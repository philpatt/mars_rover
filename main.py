from Mars import MarsPlateau


def main():
    landing_area_input = input('Please enter size of the landing plateau, separated by a space: ').split(' ')
    landing_area = MarsPlateau(int(landing_area_input[0]), int(landing_area_input[1]))

    print('landing area',landing_area)















if __name__ == "__main__":
    main()