

class Case():

    n=-1
    m=-1
    matrix = [[]]
    # Constructor
    def __init__(self,n,m,matrix):
        self.n = n
        self.m = m
        self.matrix = matrix

    # Método que calcula la distancia entre bits en el mapa
    def bits_distance(self,i1,i2,j1,j2):

        dist_i = i1 - i2
        dist_j = j1 - j2

        if dist_i<0:
            dist_i = dist_i*(-1)
        if dist_j<0:
            dist_j = dist_j*(-1)

        return dist_i+dist_j

    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    # Método que devuelve valor de la distancia más pequeña a un bit "blanco"
    def min_distance(self,i,j):

        value_i = 0
        min_value = 9999

        for row in self.matrix:

            value_j = 0
            for column in row:

                if column == 1 :
                    temp_distance = self.bits_distance(i, value_i, j, value_j)
                    if temp_distance<min_value:
                        min_value = temp_distance

                value_j += 1
            value_i += 1

        return  min_value

    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    # Método que devuelve la matriz salida ("Output")
    def output(self):
        output_matrix = []
        count_i = 0

        for row in self.matrix:
            output_row = []
            count_j = 0

            for column in row:
                output_row.append(self.min_distance(count_i,count_j))
                count_j += 1
               

            count_i += 1
            output_matrix.append(output_row)

        return output_matrix


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Métodos para cargar ficheros txt (NO PERTENECEN A LA CLASE Case)

def define_n_m_values(line):
    count_values = 0
    n_value = ''
    m_value = ''
    for letter in line:
        if letter.isdigit() and count_values == 0:
            n_value += letter
        elif not letter.isdigit():
            count_values = 1
        elif letter.isdigit() and count_values == 1:
            m_value += letter
    return [n_value, m_value]



def define_row_vector(line):
    row_result = []
    for digit in line:
        if digit.isdigit():
            row_result.append(int(digit))
    return row_result


def generate_cases():
    cases_list = []

    file = open('input.txt')
    file_lines = file.readlines()
    cases_length = int(file_lines.pop(0))


    count_cases = 0
    general_count = 0

    while (count_cases < cases_length and general_count<len(file_lines)):
        second_line_list = define_n_m_values(file_lines[general_count])
        n_value = int(second_line_list[0])
        m_value = int(second_line_list[1])
        matrix = []
        print("n = " + str(n_value))


        general_count+=1

        n_count = 0
        while (n_count<n_value and general_count<len(file_lines)):
            # print(general_count)
            current_line=file_lines[general_count]
            row = define_row_vector(current_line)
            matrix.append(row)
            n_count +=1
            general_count+=1



        count_cases = count_cases + 1
        cases_list.append(Case(n_value,m_value,matrix))

    return cases_list

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#  EJECUCIÓN MAIN


# case_A = Case(3,4,[[0,0,0,1],[0,0,1,1],[0,1,1,0]])
#
# output = case_A.output()
#
# for out in output:
#    print(out)
#
#
# print("")
#
# for i in case_A.matrix:
#    print(i)

# cases_list = generate_cases()
#
# for case in cases_list:
#     print("Cargando...")
#     output_temp = case.output()
#     for out in output_temp:
#         print(out)



def extract_elements(string_line):
    digits_list = []
    for digit in string_line:
        digits_list.append(int(digit))

    return digits_list





tests_length = int(input("Please enter the number of tests:   "))
tests_count = 0

cases_list = []
while(tests_count<tests_length):


    n = int(input("Please set the value of N:   "))
    m = int(input("Please set the value of M:   "))

    count_n = 0
    print("Now set the values of the bit map")
    print("")
    print("EXAMPLE: when n = 3 and M = 4")
    print("0001")
    print("0011")
    print("0010")
    print("")
    input_matrix = []
    while (count_n<n):

        row_list = input("Define values of row #"+str(count_n)+":   ")
        if not len(row_list) == m:
            print("Error! - The size of the array must be equal to value M")
        else:
            row_digits = extract_elements(row_list)
            input_matrix.append(row_digits)
            count_n+=1

    cases_list.append(Case(n,m,input_matrix))
    print("_________________________________________________________________________")
    tests_count+=1


for case in cases_list:
    output_value = case.output()
    for output_temp in output_value:
        print(output_temp)





