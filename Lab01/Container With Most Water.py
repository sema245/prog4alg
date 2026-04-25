class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_water = 0
        left = 0
        right = len(height) - 1

        while left < right:
            # Вычисляем текущий объем воды
            current_water = min(height[left], height[right]) * (right - left)
            max_water = max(max_water, current_water)

            # Сдвигаем указатель с меньшей высотой
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water
