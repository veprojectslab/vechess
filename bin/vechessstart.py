#!/usr/bin/env python

import vechess.core as vech

def main():
    vech.initialize()
    vech.BoardState_clear()
    vech.BoardState_populate_from_single_dict({"cmd": "", "id": None, "KW": "E1", "QW": "D1", "R1W": "A1", "N1W": "B1", "B1W": "C1", "R2W": "H1", "N2W": "G1", "B2W": "F1", "P1W": "A2", "P2W": "B2", "P3W": "C2", "P4W": "D2", "P5W": "E2", "P6W": "F2", "P7W": "G2", "P8W": "H2", "KB": "E8", "QB": "D8", "R1B": "H8", "N1B": "G8", "B1B": "F8", "R2B": "A8", "N2B": "B8", "B2B": "C8", "P1B": "H7", "P2B": "G7", "P3B": "F7", "P4B": "E7", "P5B": "D7", "P6B": "C7", "P7B": "B7", "P8B": "A7", })
    print(vech.BoardState_data())

if __name__ == "__main__":
    main()
