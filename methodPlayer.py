import sys
import time
import wave


def intChange(strChange):
    change = []
    for bell in strChange.split():
        if bell == "0":
            bell = 10
        elif bell == "E":
            bell = 11
        elif bell == "T":
            bell = 12
        else:
            bell = int(bell)
        change.append(bell)
    return(change)


def methodPlayer(printout):
    f = open("text/%s.txt" % (printout))
    stage = int(f.readline())
    rows = f.readlines()
    if stage % 2 == 1:  # add a cover for odd bell methods
        stage += 1
        new_rows = []
        for row in rows:
            row = row[:-1] + "%d\n" % (stage)
            new_rows.append(row)
        rows = new_rows

    data = []

    def add_row(row, handstroke):
        for bell in intChange(row):
            tone = "input_tones/%d.wav" % (stage + 1 - bell)
            w = wave.open(tone, 'rb')
            data.append([w.getparams(), w.readframes(w.getnframes())])
            w.close()
        if handstroke:
            data.append([w.getparams(), b'\x00' * 6000])

    # writes rounds an extra time before starting
    add_row(rows[0], False)
    handstroke = True
    for row in rows:  # then write all the rows, with handstroke pauses
        add_row(row, handstroke)
        handstroke = not handstroke
    add_row(rows[0], False)
    add_row(rows[0], True)

    output = wave.open("output_audio/out.wav", 'wb')
    output.setparams(data[0][0])
    for sound in data:
        output.writeframes(sound[1])
    output.close()


if __name__ == "__main__":
    methodPlayer(str(sys.argv[1]))
