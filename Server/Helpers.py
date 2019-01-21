class Helpers:

    @staticmethod
    def generate_list(res):
        data_list = []
        for _row in res:
            row_as_dict = dict(_row)
            data_list.append(row_as_dict)
        return data_list
