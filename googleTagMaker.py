with open('2tagfile', 'r') as d2:
    for j in d2.readlines():
        with open('3tagfile', 'r') as d3:
            for k in d3.readlines():
                with open(j, 'a') as d4:
                    d4.write('phone number ' + j.replace('\n', '') + ' in ' + k.replace('\n', '') + '\n')
