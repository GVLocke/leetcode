class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var prevMap = [Int:Int]()
        for (index, value) in nums.enumerated() {
            if let diff = prevMap[value] {
                return [diff, index]
            } else {
                prevMap[target - value] = index
            }
        } 
        return []
    }
}

let bruh: Solution = Solution()
let nums = [3,2,4]
print(bruh.twoSum(nums, 6))