class Solution {
    func containsDuplicate(_ nums: [Int]) -> Bool {
        var nums_set = Set<Int>()
        for i in nums {
            if nums_set.contains(i) {
                return true
            } else {
                nums_set.insert(i)
            }
        }
        return false
    }
}

let bruh = Solution()
let list = [1,2,3,4,5,6,7,8,9,10]
print(bruh.containsDuplicate(list))