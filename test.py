from board import Board

def test_rules():
    # Rules:

    # 1: dead cells with no live neighbours should stay dead

    # boards are generated
    mb = Board(4, 4) # main board
    tb = Board(4, 4) # test board

    mb.update()

    if str(mb) == str(tb):
        print("Rule 1 is ok")
    else:
        print("Error with rule 1.")
        print(f"Expected:\n{str(tb)}")
        print(f"Got:\n{str(mb)}")


    # 2: living cells with less than 2 neighbours alive die

    # boards are generated again

    # initial:
    mb.generate(
        [
            [1, 0, 0, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 0, 0, 1]
        ]
    )

    # expected:
    tb = Board(4, 4)

    mb.update()

    if str(mb) == str(tb):
        print("Rule 2 is ok")
    else:
        print("Error with rule 2.")
        print(f"Expected:\n{str(tb)}")
        print(f"Got:\n{str(mb)}")


    # 3: living cells with 2 or 3 live neighbours stay alive

    # boards are generated again

    # initial:
    mb.generate(
        [
            [1, 1, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 1, 1, 1]
        ]
    )

    # expected:
    tb.generate(
        [
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 0]
        ]
    )

    mb.update()

    if str(mb) == str(tb):
        print("Rule 3 is ok.")
    else:
        print("Error with rule 3.")
        print(f"Expected:\n{str(tb)}")
        print(f"Got:\n{str(mb)}")

    # 4: living cells with more than 3 neighbours die

    # boards are generated again

    # initial
    mb.generate(
        [
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 1, 1],
            [0, 0, 1, 1]
        ]
    )

    # expected:
    tb.generate(
        [
            [1, 1, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 1]
        ]
    )

    mb.update()

    if str(mb) == str(tb):
        print("Rule 4 is ok.")
    else:
        print("Error with rule 4.")
        print(f"Expected:\n{str(tb)}")
        print(f"Got:\n{str(mb)}")

    # 5: dead cells with exactly 3 neighbours become alive

    # boards are generated again

    # initial
    mb.generate(
        [
            [1, 1, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 1]
        ]
    )

    # expected:
    tb.generate(
        [
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 1, 1],
            [0, 0, 1, 1]
        ]
    )

    mb.update()

    if str(mb) == str(tb):
        print("Rule 5 is ok.")
    else:
        print("Error with rule 5.")
        print(f"Expected:\n{str(tb)}")
        print(f"Got:\n{str(mb)}")

    
def test_pattern(pattern: list):
    b = Board(0, 0)
    b.generate(pattern)
    
    from time import sleep 
    import os

    while True:
        sleep(0.25)
        
        os.system('cls')
        b.update()
        print(b)

if __name__ == '__main__':
    toad_pattern = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]

    blinker_pattern = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
    ]

    beacon_pattern = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    test_pattern(beacon_pattern)