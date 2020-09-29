# A password is considered strong if below conditions are all met:
#
# It has at least 6 characters and at most 20 characters.
# It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.
# It must NOT contain three repeating characters in a row ("...aaa..." is weak, but "...aa...a..." is strong,
# assuming other conditions are met).
# Write a function strongPasswordChecker(s), that takes a string s as input,
# and return the MINIMUM change required to make s a strong password. If s is already strong, return 0.
#
# Insertion, deletion or replace of any one character are all considered as one change.
#


class Solution:
    """
    암호는 아래 조건이 모두 충족될 경우 강력한 것으로 간주된다.

    최소 6자 이상, 최대 20자 이상이다.
    하나 이상의 소문자, 하나 이상의 대문자 및 하나 이상의 숫자를 포함해야 한다.
    연속된 세 개의 반복 문자("...aaa...)를 포함할 수 없다."는 약하지만 "...a...a..."는 다른 조건이 충족된다고 가정하면 강하다.)

    문자열을 입력으로 사용하는 함수 strongPasswordChecker를 작성하고 강력한 암호를 만드는 데 필요한 최소 변경사항을 반환하십시오. s가 이미 강한 경우 0을 반환하십시오.

    한 문자를 삽입, 삭제 또는 교체하는 것은 모두 하나의 변경으로 간주된다.
    """

    def strongPasswordChecker(self, s: str) -> int:

        missing_type = 3
        if any('a' <= char <= 'z' for char in s): missing_type -= 1
        if any('A' <= char <= 'Z' for char in s): missing_type -= 1
        if any(char.isdigit() for char in s): missing_type -= 1

        replace = 0
        one = two = 0  # ?
        i = 2
        while i < len(s):
            if s[i] == s[i - 1] == s[i - 2]:  # aaa 연속되면
                duplicated_length = 2
                while i < len(s) and s[i] == s[i - 1]:
                    duplicated_length += 1
                    i += 1

                replace += duplicated_length // 3  # every 3번째 마다 1개씩 교체
                if duplicated_length % 3 == 0:  # aaxaaxaax  9   one
                    one += 1
                elif duplicated_length % 3 == 1:  # bbxbbxbzzzbbxb 10   two
                    two += 1

            else:
                i += 1

        if len(s) < 6:
            return max(6 - len(s), missing_type)

        elif len(s) <= 20:
            return max(missing_type, replace)

        else:
            delete = len(s) - 20  # 일단 넘치는 개수. 결국 이 만큼은 무조건 빼줘야 함.     len(s)= 24  one = 5

            # replace = aaa -> aax 로 교체하려는 x의 개수.  3으로 나눈 몫의 개수. 이미 계산해놓은 것.
            # 여기서 replace 개수만큼 다 바꿀 필요 없이 delete 겸용으로 해서 빼주면 되는 것들이 있고 그걸 빼고 delete 예산에서 빼주면 replace 할당량에서는 빼줘야 함.

            replace -= min(delete, one)  # 원래 빼야 할 개수와 연속수 중 끝 1개를 빼면 되는 개수(연속된 개수가 3의 배수인 것) 중에 비교해서 더 적은 수를 빼줌.
            # ex) len(s)= 24  delete: 4 < one: 5 이면 one을 4만큼을 빼줌. 4만큼은 x로 replace할 필요 없이 그냥 삭제해버리면 되는 것.
            replace -= min(max(delete - one, 0), two * 2) // 2
            replace -= max(delete - one - 2 * two, 0) // 3

            return delete + max(missing_type, replace)

    """
    6개보다 적거나, 6개 <= s <= 20개는 쉽다. 
    len > 20일 때 len - 20회 삭제를 해야 한다. 
    또한 우리는 3개의 반복 캐릭터마다 변화를 줄 필요가 있다.

    len % 3 == 0의 반복 시퀀스에 대해, 하나의 문자를 삭제하여 하나의 대체 문자를 줄일 수 있다. 
    len % 3 == 1의 반복 시퀀스에 대해, 우리는 2개의 문자를 삭제함으로써 하나의 대체 문자를 줄일 수 있다. 
    나머지 시퀀스에 대해서는 3자를 삭제하면 모든 교체를 줄일 수 있다.


문자열 길이가 20자 이상일 경우 일부 문자를 삭제해야 하며 적절한 삭제는 삭제 후 반복 시퀀스를 깨는 데 필요한 교체 횟수를 줄일 수 있다. len % 3 == 0으로 반복되는 시퀀스의 경우 len/3을 교체해야 하며, 한 문자를 삭제하여 len/3으로 교체하는 횟수를 하나씩 줄일 수 있다. 마찬가지로, len % 3 == 1의 반복 시퀀스에 대해, 우리는 두 문자를 삭제함으로써 하나의 대체물을 줄일 수 있다. 이제 우리는 이미 삭제된 문자를 포함하여 모든 시퀀스에 대해 len % 3 == 2를 가지고 있으므로 모든 삭제 작업이 중요하도록 세 문자를 삭제함으로써 모든 대체 항목을 줄일 수 있다는 것을 안다.

왜냐하면, 예를 들어, 삭제할 문자가 10자(예: 삭제 = 10)인 경우, 2개의 모든 대체 문자를 2개의 삭제로 대체할 수 있기 때문이다. 따라서 10의 삭제 예산으로 유형 2의 대체품(렌 % 3 == 1인 경우)을 최대 (10/2)=5개까지 줄일 수 있다. 같은 논리가 3으로 나누어져도 적용된다.
    """


# 42 / 42 test cases passed.
# Status: Accepted
# Runtime: 28 ms
# Memory Usage: 14.1 MB
#
# Your runtime beats 77.92 % of python3 submissions.
# Your memory usage beats 7.06 % of python3 submissions.

