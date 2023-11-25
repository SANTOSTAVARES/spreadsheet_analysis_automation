from time import sleep
from domain.routine import analyze_sheet_and_record_cheking_into_db


def main():
    while True:
        analyze_sheet_and_record_cheking_into_db()
        sleep(60 * 30)


if __name__ == "__main__":
    main()
