from marvel import full_dict

check_sort = list(sorted(full_dict.items(), key=lambda x: x[1]['title']))


def sort_dict(word: str, reverse=False) -> dict:

    try:
        new_sort_dict = dict(sorted(full_dict.items(), key=lambda x: int(x[1][word]) if word == 'year' else x[1][word], reverse=reverse))
        return new_sort_dict
    except KeyError:
        print(f'{word} is not found in the dictionary')


print(sort_dict('title'))
