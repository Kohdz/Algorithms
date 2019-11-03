nums = [2, 7, 11, 15];
target = 9;

function twoSum(nums, target) {
  let dict = {};
  for (let i = 0; i < nums.length - 1; i++) {
    diff = target - nums[i];
    if (!(diff in dict)) {
      dict[nums[i]] = i;
    } else {
      return [dict[target - nums[i]], i];
    }
  }
}

console.log(twoSum(nums, target));

// for (let step = 0; step < 5; step++) {
