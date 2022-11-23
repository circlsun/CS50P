time = input('What time is it? ')

def main():
    if 7.0 <= convert(time) <= 8.0:
        print('breakfast time')
    if 12.0 <= convert(time) <= 13.0:
        print('lunch time')
    if 18.0 < convert(time) < 19.0:
        print('dinner time')

def convert(time):
   time = time.replace(':', '.')
   time = float(time[:-1])
   return time

if __name__ == "__main__":
    main()