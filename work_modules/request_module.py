import requests


url_api = 'http://api.open-notify.org/astros.json'


def raw_astro_data():
    """
    function tries to open api and prepare data for following processing
    """
    try:
        response = requests.get(url_api, timeout=5)
        response.raise_for_status()
        print(response)
    except requests.exceptions.HTTPError as error:
        print(error)
        return None
    except requests.exceptions.ConnectionError as error:
        print(error)
        return None
    except requests.exceptions.Timeout as error:
        print(error)
        return None
    except requests.exceptions.RequestException as error:
        print(error)
        return None

    ppl = response.json()
    astro_list_data_raw = ppl['people']

    return astro_list_data_raw


def all_astros_in_space() -> list:
    """
    returns the list of astronauts, that currently inhabit all the space crafts
    """
    astro_list_data_raw = raw_astro_data()
    if astro_list_data_raw:  # if someone in space now and we can collect the data
        astro_list_data = []

        for astro in astro_list_data_raw:
            astro_list_data.append(astro['name'])

        return astro_list_data
    else:
        return None


def astros_on_defined_craft() -> dict:
    """
    returns the list of astronauts, grouped by they space crafts
    """
    astro_list_data_raw = raw_astro_data()

    if astro_list_data_raw:  # if someone in space now and we can collect the data
        # here we extract all names of crafts with people in the space like list of lists
        list_of_craft = list()
        for item in astro_list_data_raw:
            if item['craft'] not in list_of_craft:
                list_of_craft.append([item['craft']])

        # here we create the set with the unique names of space crafts
        list_of_craft_clear = list()
        for i in range(len(list_of_craft)):
            list_of_craft_clear.append(list_of_craft[i][0])
        list_of_craft_clear = set(list_of_craft_clear)

        # here we create a dict, where the keys - names of crafts, value - empty list, where we add later people
        astro_on_craft = dict()
        for item in list_of_craft_clear:
            astro_on_craft[item] = []

        # here we define all the people from the appropriate space craft
        for item in astro_list_data_raw:
            astro_on_craft[item['craft']] = astro_on_craft[item['craft']] + [item['name']]

        return astro_on_craft
    else:
        return None


if __name__ == "__main__":
    print(f'All the people in space now: {all_astros_in_space()}')