class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_ptr, typed_ptr = 0, 0

        if name[-1] != typed[-1]:
            return False

        while name_ptr < len(name) and typed_ptr < len(typed):
            count_name = 1
            count_typed = 1

            if name_ptr < len(name) - 1 and name[name_ptr] == name[name_ptr + 1]:
                # Count the consecutive occurrences of the character in name
                while name_ptr < len(name) - 1 and name[name_ptr] == name[name_ptr + 1]:
                    count_name += 1
                    name_ptr += 1

            if typed_ptr < len(typed) - 1 and typed[typed_ptr] == typed[typed_ptr + 1]:
                # Count the consecutive occurrences of the character in typed
                while typed_ptr < len(typed) - 1 and typed[typed_ptr] == typed[typed_ptr + 1]:
                    count_typed += 1
                    typed_ptr += 1

            if name[name_ptr] != typed[typed_ptr] or count_typed < count_name:
                return False

            name_ptr += 1
            typed_ptr += 1

        return name_ptr == len(name) and typed_ptr == len(typed)