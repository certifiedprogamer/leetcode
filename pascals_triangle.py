class Solution(object):
    def generate(self, numRows):
        triangle = [[1]]
        for i in range(numRows - 1):
            triangle_layer = []
            triangle_layer.append(1)
            for itr in range(len(triangle[i])):
                try:
                    triangle_layer.append(
                        triangle[i][itr] + triangle[i][itr + 1])
                except:
                    pass
            triangle_layer.append(1)
            triangle.append(triangle_layer)
        return triangle


print(Solution.generate(1, 5))
