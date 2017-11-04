if __name__ == '__main__':
    with open('sample.rain') as f:
        raw_rain_data = f.readlines()
        raw_rain_data = [line.strip() for line in raw_rain_data]

    for index, line in enumerate(raw_rain_data):
        if set(line) == set('-'):
            raw_rain_data = raw_rain_data[index +1::]
            break

    for data_point in raw_rain_data:
        data = data_point.split(' ')
        data = [item for item in data if item is not '']

        # if '-' in data:
        #     print(f"Invalid rain data for date {data[0]}!")
        print[data 1:]
