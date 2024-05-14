# List
my_list = [1, 2, 3, 4, 5]

# Tuple
my_tuple = (1, 2, 3, 4, 5)

# Set
my_set = {1, 2, 3, 4, 5}

# Dict
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# 장점과 단점 비교 함수
def compare_advantages_disadvantages(data_structure):
    advantages = []
    disadvantages = []

    # 장점
    if isinstance(data_structure, (list, tuple, set, dict)):
        advantages.append("데이터 구조에 따라 유연한 사용 가능")

    if isinstance(data_structure, (list, tuple, set)):
        advantages.append("순회 가능")

    if isinstance(data_structure, (list, tuple, set)):
        advantages.append("값 변경 가능")

    if isinstance(data_structure, (list, tuple, dict)):
        advantages.append("인덱싱 및 슬라이싱 가능")

    if isinstance(data_structure, (list, tuple, set)):
        advantages.append("중복 요소 제거 (Set)")

    if isinstance(data_structure, (list, set, dict)):
        advantages.append("크기가 동적으로 조절 가능")

    # 단점
    if isinstance(data_structure, list):
        disadvantages.append("검색 및 삽입, 삭제 시간복잡도가 높음")

    if isinstance(data_structure, tuple):
        disadvantages.append("값 변경 불가능")

    if isinstance(data_structure, set):
        disadvantages.append("순서가 없어 인덱싱이 불가능")

    if isinstance(data_structure, dict):
        disadvantages.append("키가 중복되면 덮어씌워짐")

    return advantages, disadvantages

# List 장단점 비교
list_advantages, list_disadvantages = compare_advantages_disadvantages(my_list)
print("List의 장점:", list_advantages)
print("List의 단점:", list_disadvantages)

# Tuple 장단점 비교
tuple_advantages, tuple_disadvantages = compare_advantages_disadvantages(my_tuple)
print("Tuple의 장점:", tuple_advantages)
print("Tuple의 단점:", tuple_disadvantages)

# Set 장단점 비교
set_advantages, set_disadvantages = compare_advantages_disadvantages(my_set)
print("Set의 장점:", set_advantages)
print("Set의 단점:", set_disadvantages)

# Dict 장단점 비교
dict_advantages, dict_disadvantages = compare_advantages_disadvantages(my_dict)
print("Dict의 장점:", dict_advantages)
print("Dict의 단점:", dict_disadvantages)
