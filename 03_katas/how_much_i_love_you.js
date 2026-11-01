function howMuchILoveYou(nbPetals) {
  const sweets = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"];
  return sweets[(nbPetals - 1) % 6];
}
console.log(howMuchILoveYou(3));
