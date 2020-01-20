function reverseString(str) {
    if(!str || str.length < 2 || typeof str !== "string") 
        return "That's not going to work"

    return str.split('')
              .reverse()
              .join('')
}

console.log(reverseString(12))