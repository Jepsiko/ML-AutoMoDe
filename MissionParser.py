

MISSION_FILE = '/home/apierrot/MissionGeneratorMG1/generated_missions/all_missions.txt'
INPUT_FILE = '/home/apierrot/ML-AutoMoDe/input.txt'

MAX_DURATION = 180
MAX_ROBOTS = 20

INPUT_NAMES = [
    'Foraging',
    'Homing',
    'Aggregation-XOR',
    'Duration',
    '#Robots',
    'Triangle',
    'Square',
    'Hexagon',
    'Uniform',
    'One-side',
    'Not-on-colored-areas',
    'Left',
    'Right',
    'Light',
    'Color',
    # '#Obstacles',
    # 'Anytime',
    # 'Endtime',
    # '#Nests',
    # '#Food-sources',
    # '#Colored-areas',
    # '#Aggregation-areas',
    # '#Distraction-areas',
]


def get_mission_parameters(line):
    line = line.strip().split(' ')
    line = list(filter(lambda x: x != '', line))
    parameters = {}
    last_param = None
    for elem in line:
        if elem[:2] == '--':
            parameters[elem] = []
            last_param = elem
        else:
            elem = elem.strip("'")
            try:
                elem = float(elem)
            except ValueError:
                pass
            parameters[last_param].append(elem)
    return parameters


def initialize_inputs():
    inputs = {}
    for name in INPUT_NAMES:
        inputs[name] = 0
    return inputs


def parse_mission_type(inputs, params):
    mission_type = params['--m'][0]
    if mission_type == 'foraging':
        inputs['Foraging'] = 1
    elif mission_type == 'homing':
        inputs['Homing'] = 1
    elif mission_type == 'aggXOR':
        inputs['Aggregation-XOR'] = 1
    else:
        raise ValueError


def parse_duration(inputs, params):
    duration = params['--el'][0]
    inputs['Duration'] = duration / MAX_DURATION


def parse_robots_count(inputs, params):
    robots_count = params['--r'][0]
    inputs['#Robots'] = robots_count / MAX_ROBOTS


def parse_shape_arena(inputs, params):
    shape_arena = params['--a'][0]
    if shape_arena == 'trigon':
        inputs['Triangle'] = 1
    elif shape_arena == 'tetragon':
        inputs['Square'] = 1
    elif shape_arena == 'hexagon':
        inputs['Hexagon'] = 1
    else:
        raise ValueError


def parse_side(inputs, params):
    side = params['--ip'][1]
    if side == 0:
        inputs['Left'] = 1
    elif side == 1:
        inputs['Right'] = 1
    else:
        raise ValueError


def parse_initial_distribution(inputs, params):
    initial_distribution = params['--ip'][0]
    if initial_distribution == 'uniform':
        inputs['Uniform'] = 1
    elif initial_distribution == 'oneside':
        inputs['One-side'] = 1
        parse_side(inputs, params)
    elif initial_distribution == 'notpatches':
        inputs['Not-on-colored-areas'] = 1
    else:
        raise ValueError


def parse_light(inputs, params):
    light = params['--l'][0]
    if light == 'on':
        inputs['Light'] = 1


def parse_color(inputs, params):
    if '--colhome' in params:
        color = params['--colhome'][0]
    elif '--colnest' in params:
        color = params['--colnest'][0]
    else:
        raise ValueError
    if color == 'black':
        inputs['Color'] = 1


def parse_mission_parameters(params):
    inputs = initialize_inputs()
    parse_mission_type(inputs, params)
    parse_duration(inputs, params)
    parse_robots_count(inputs, params)
    parse_shape_arena(inputs, params)
    parse_initial_distribution(inputs, params)
    parse_light(inputs, params)
    parse_color(inputs, params)
    return inputs


if __name__ == '__main__':
    with open(MISSION_FILE) as m, open(INPUT_FILE, 'w') as i:
        for line in m.readlines():
            mission_params = get_mission_parameters(line)
            inputs = parse_mission_parameters(mission_params)
            print(inputs)
            values = [str(v) for v in inputs.values()]
            i.write(' '.join(values) + '\n')