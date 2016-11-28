import sys
import re


def strChange(arrChange):
    change = ""
    for bell in arrChange:
        if bell == 10:
            b = "0"
        elif bell == 11:
            b = "E"
        elif bell == 12:
            b = "T"
        else:
            b = str(bell)
        change = change + b + " "
    return change


def pNoteExpander(pNote):
    pNote = pNote.split("_")
    lead = pNote[0].split(".")
    if len(pNote) > 1:
        leadEnd = pNote[1][1:]
        lead = lead[:-1]+lead[::-1]+[leadEnd]
    newLead = []
    for change in lead:
        newChange = []
        change = list(change)
        for place in change:
            if place == "0":
                newChange.append(10)
            elif place == "E":
                newChange.append(11)
            elif place == "T":
                newChange.append(12)
            elif place != "x":
                newChange.append(int(place))
        newLead.append(newChange)
    return newLead


def getStage(stage):
    if stage == "E" or stage == "e":
        return 11
    elif stage == "T" or stage == "t":
        return 12
    elif stage == "0":
        return 10
    else:
        return int(stage)


def pnRegularizer(pNote, stage):
    if stage == "10":
        stage = "0"
    elif stage == "11":
        stage = "E"
    elif stage == "12":
        stage = "T"
    else:
        stage = str(stage)

    pNote = pNote.replace(" ", "_")
    pNote = pNote.replace("e", "E")
    pNote = pNote.replace("t", "T")
    pNote = pNote.replace("h", "1.")
    pNote = re.sub(r'([ET\d])(?=[xh-])', r'\g<0>.', pNote)
    # print(pNote)

    if getStage(stage) % 2 == 0:
        pNote = re.sub(r'[x-]', "x.", pNote)
        pNote = re.sub(r'([13579E])(?=\.)', r'\g<0>'+stage, pNote)
    else:
        pNote = re.sub(r'[x-]', stage+".", pNote)
        pNote = re.sub(r'([24680T])(?=\.)', r'\g<0>'+stage, pNote)
    # print(pNote)

    pNote = re.sub(r'(?<=[^\.l])1', r'.1', pNote)
    pNote = re.sub(r'(?<=[^\dET])([24680T])', r'1\g<1>', pNote)
    pNote = re.sub(r'^([24680T])', r'1\g<1>', pNote)
    # print(pNote)

    pNote = re.sub(r'\.*(?=[\s_\b]|$)', "", pNote)
    # print(pNote)

    return pNote


def methodPrinter(pNote, stage):
    stageN = getStage(stage)
    lead = pNoteExpander(pNote)

    f = open("text/%s_%s.txt" % (pNote, stage), "w")
    f.write(str(stageN)+"\n")

    rounds = list(range(1, stageN+1))
    curChange = list(range(1, stageN+1))

    handstroke = True  # not used yet, but just in case for later
    while True:
        handstroke = False if handstroke else True
        for change in lead:
            # print(strChange(curChange))
            f.write(strChange(curChange)+"\n")
            i = 0
            while i < len(rounds)-1:
                if (i + 1) in change:
                    i += 1
                else:
                    curChange[i], curChange[i+1] = curChange[i+1], curChange[i]
                    i += 2
        if curChange == rounds:
            # print(strChange(curChange))
            f.write(strChange(curChange)+"\n")
            break
    f.close()


def notationReader(pNote, stage):
    try:
        pNote = pnRegularizer(pNote, stage)
    except ValueError:
        return -1
    # print(pNote)
    try:
        methodPrinter(pNote, stage)
        return "%s_%s" % (pNote, stage)
    except ValueError:
        return -1

if __name__ == "__main__":
    print(notationReader(str(sys.argv[1]), str(sys.argv[2])))
