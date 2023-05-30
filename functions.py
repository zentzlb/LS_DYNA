def get_nextline(text, c: int = 0):
    """
    grab next line of text from string
    :param text: (string)
    :param c: (int)
    :return: line (string)
    """

    ind1 = text.find('\n', c)
    ind2 = text.find('\n', ind1 + 1)
    if ind1 != -1 and ind2 != -1:
        return text[ind1 + 1:ind2], ind2
    else:
        return None


def parse_line(line: str):
    """
    convert line of text to list
    :param line: (string)
    :return: list (list)
    """
    line_list = line.split(' ')
    line_list = [i for i in line_list if i != '']
    return line_list


def open_key(file_path: str):
    """
    open key file and convert to string
    :param file_path: (string)
    :return: text (string)
    """
    with open(file_path, 'r') as file:
        text = file.read()
    return text


def get_nodes(text):
    """
    extract shell elements from string
    :param text: (string)
    :return: nodes: (dictionary)
    """
    nodes = {}
    inds = text.find('*NODE')
    indf = text.find('*', inds + 1)
    node_text = text[inds:indf]
    c = 0
    while c < len(node_text) - 1:
        new_line, c = get_nextline(node_text, c)
        new_list = parse_line(new_line)
        if len(new_list) > 0 and new_list[0].isalnum():
            node = {'x': float(new_list[1]), 'y': float(new_list[2]), 'z': float(new_list[3])}
            nodes[f'{new_list[0]}'] = node
        print(c)
    return nodes


def get_shell(text: str):
    """
    extract shell elements from string
    :param text: (string)
    :return: elements (dictionary)
    """
    elements = {}
    inds = text.find('*ELEMENT_SHELL')
    indf = text.find('*', inds + 1)
    shell_text = text[inds:indf]
    shell_text = shell_text.replace('MECH', '')
    c = 0
    while c < len(shell_text) - 1:
        new_line, c = get_nextline(shell_text, c)
        new_list = parse_line(new_line)
        if len(new_list) > 0 and new_list[0].isalnum():
            shell = {'n1': new_list[2], 'n2': new_list[3], 'n3': new_list[4], 'n4': new_list[5]}
            elements[f'{new_list[0]}'] = shell
        print(c)
    return elements


def get_part_ids(text):
    """
    extract shell elements from string
    :param text: (string)
    :return: part_ids: (list)
    """
    part_ids = []
    inds = 0
    while text.find('*PART\n', inds) != -1:
        inds = text.find('*PART\n', inds)
        indf = text.find('*', inds + 1)
        part_text = text[inds:indf]
        c = 0
        while c < len(part_text) - 1:
            new_line, c = get_nextline(part_text, c)
            new_list = parse_line(new_line)
            if len(new_list) > 0 and new_list[0].isnumeric():
                print(new_list)
                part_ids.append(new_list[0])
                # node = {'x': float(new_list[1]), 'y': float(new_list[2]), 'z': float(new_list[3])}
                # nodes[f'{new_list[0]}'] = node
        inds = indf
    return part_ids


def check_shell(shell: dict, nodes: dict, equation: str, tolerance: float):
    """
    Check if shell element nodes satisfy equation
    :param shell: shell element (dictionary)
    :param nodes: all nodes (dictionary)
    :param equation: equation all shell element nodes must satisfy (string)
    :param tolerance: tolerance for nodes satisfying equation (float)
    :return: True if check passes, False otherwise
    """
    check = True
    for nid in shell.keys():
        node = nodes[shell[nid]]
        x = node['x']
        y = node['y']
        z = node['z']
        if abs(eval(equation)) > tolerance:
            check = False
    return check


def check_node(node: dict, equation: str, tolerance: float):
    """
    Check if shell element nodes satisfy equation
    :param node: a node (dictionary)
    :param equation: equation node must satisfy (string)
    :param tolerance: tolerance for node satisfying equation (float)
    :return: True if check passes, False otherwise
    """
    check = True
    x = node['x']
    y = node['y']
    z = node['z']
    if abs(eval(equation)) > tolerance:
        check = False
    return check


def make_new_element_set(file_path: str, new_file_path: str, equation: str, tolerance: float = 0.1, pid: int = 1):
    """
    create new key file
    :param file_path: path to original key file (string)
    :param new_file_path: path to new key file (string)
    :param equation: equation all shell element nodes must satisfy (string)
    :param tolerance: tolerance for nodes satisfying equation (float)
    :param pid: part ID (integer)
    """
    text = open_key(file_path)
    nodes = get_nodes(text)
    elements = get_shell(text)

    newfile_text = '*ELEMENT_SHELL\n$    EID     PID      N1      N2      N3      N4\n$#   eid     pid      n1      n2      n3      n4\n'
    for key in elements.keys():
        element = elements[key]
        if check_shell(element, nodes, equation, tolerance):
            temp = f'{key:>8}{pid:>8}{element["n1"]:>8}{element["n2"]:>8}{element["n3"]:>8}{element["n4"]:>8}\n'
            newfile_text += temp
            print(temp)
    newfile_text += '*END\n'

    with open(new_file_path, 'w') as my_text:
        my_text.write(newfile_text)  # save key file


def make_new_part_set(file_path: str, new_file_path: str, sid: int = 1, name: str = 'All_Parts'):
    """
    create new key file
    :param file_path: path to original key file (string)
    :param new_file_path: path to new key file (string)
    :param sid: part ID (integer)
    :param name: name of part set (string)
    """
    text = open_key(file_path)
    parts = get_part_ids(text)

    newfile_text = f'*SET_PART_LIST_TITLE\n{name}\n$#     sid       da1       da2       da3       da4    solver      \n{sid:>10}       0.0       0.0       0.0       0.0MECH\n$#    pid1      pid2      pid3      pid4      pid5      pid6      pid7      pid8\n'

    n = len(parts) % 8
    if n != 0:
        for i in range(n, 8):
            parts.append('0')
    rows = len(parts) // 8

    for row in range(rows):
        for i in range(8):
            temp = f'{parts[row * 8 + i]:>10}'
            newfile_text += temp
        newfile_text += '\n'
    newfile_text += '*END\n'

    with open(new_file_path, 'w') as my_text:
        my_text.write(newfile_text)  # save key file

    return newfile_text
