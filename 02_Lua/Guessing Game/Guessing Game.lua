math.randomseed(os.time()) -- Seed the random number generator

-- Function to run a single game
function play_game()
    local secret_number = math.random(1, 100)
    local max_attempts = 7
    local attempts = 0
    local has_won = false

    print("Guess the number between 1 and 100. You have 7 attempts.")

    while attempts < max_attempts do
        io.write("Enter your guess: ")
        local guess = tonumber(io.read())
        attempts = attempts + 1

        if guess == secret_number then
            print("Congratulations! You guessed the number in " .. attempts .. " attempts.")
            has_won = true
            break
        elseif guess < secret_number then
            print("Too low. Try again.")
        elseif guess > secret_number then
            print("Too high. Try again.")
        else
            print("Invalid input. Please enter a number.")
        end
    end

    if not has_won then
        print("Sorry, you lost. The correct number was " .. secret_number .. ".")
    end
end

-- Main game loop
while true do
    play_game()

    io.write("Do you want to play again? (yes/no): ")
    local response = io.read():lower()
    if response ~= "yes" then
        print("Thanks for playing!")
        break
    end
end
