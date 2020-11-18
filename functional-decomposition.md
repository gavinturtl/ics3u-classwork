# Functional Decomposition

## Getting food from a vending machine

### Vending machine from a human perspective (in-class example)

You get a bag of chips from a vending machine.
- Approach machine
    - Walk until you are within arms reach
- Determine the number for the flavour I want.
    - Search for the specific flavour
    - Look just below it for the ID number. (Remember that number)
- Put in appropriate amount of money.
    - Look beside the ID number for the cost of the snack
    - Get out some money greater or equal to that amount.
    - Place that money into the intake.
- Key in the number for the flavour.
- Get bag from bottom of machine.
    - Bend down
    - Put arm through slot
    - Grab chips
    - Pull your arm out (with the chips)

### Vending machine from the machine's perspective

You vend a bag of chips to a human.
- Wait for human to put in money
    - Give instructions to human to insert money into machine.
    - Accept the human's bill(s)/coin(s) through their designated slots.
    - Scan money for validity.
    - If money is valid, organize bills/coins individually into their specific storage compartments based on their type/amount.
    - Else, reject invalid bill from slot or drop invalid coins into the change compartment.
- Wait for human to key in item ID number.
    - After money is accepted, instruct human to key in their desired item's ID number.
    - If amount of money is insufficient for the chosen item, inform human of the insufficiency.
    - If item is out of stock, inform human that item is out of stock.
    - Else, proceed to process transaction.
- Refer to ID number and push bag of chips over the edge.
    - Activate rotating spring in the keyed-in ID number's slot.
    - Repeat 360 degree rotations until chip bag falls into retrieval compartment.
- Wait for human to retrieve bag from slot.
    - After chip bag is dropped, thank human and tell human to have a nice day.
    - Then, prepare instructions again for the next human to put in money.

### Identify where there might be basic programming concepts in your break-down above.

- Displaying instructions may require simple commands that make certain pixels light up and/or move right to left for longer sentences.
- Displaying instructions may require a loop that will stop/change once the instructions are followed.
- Ensuring that the money is valid may require an if/else statement.
- Ensuring that the money is sufficient may also require an if/else statement.
- Organizing the change/bills into their individually organized slots may require if/else statements.
- Checking to see that the desired item is still in stock may also require an if/else statement.
- The rotating spring may require a simple command to rotate clockwise/counter clockwise.
- The rotating spring may require a loop that will stop rotations when the chip bag successfully falls into the retrieval slot.


## The cookie is too big for the glass

### How do you fix this problem?

Break part of the cookie off bit by bit until it fits.
- Take the cookie.
    - Use your fingers to grip the cookie
    - Take the cookie out of the glass.
- Break off a small part of the cookie.
    - Grip most of the cookie in one hand and a small part of the cookie in the other hand.
    - Use your fingers to break off a small section of the cookie.
    - Eat/set aside the small broken piece of cookie.
- Try to fit cookie into glass.
    - Take the now slightly smaller cookie.
    - Try to fit the cookie into the glass.
    - If you are satisfied with how the cookie fits, problem solved.
    - Else, repeat the "Break off a small part of the cookie." step, testing if the cookie fits after each repetition, until you are satisfied/the cookie fits.
    
### How can you prevent this problem?

Buy bigger glasses.
- Find the average greatest possible diameter of your cookies.
    - If you have equal or less than two dozen cookies, select the biggest cookies until you've selected half of your total amount.
    - If you have more than two dozen cookies, select the biggest cookies until you've selected a third or a quarter of your total amount.
    - Get a ruler.
    - Find the average diamater (cm) of your biggest selected cookies to use as reference for the diameter of your to-be-purchased glass(es).
    - Round up to a whole number and remember that measurement. We'll call it "COOKIE"
- Go to the store (one that sells drinking glasses)
    - Take your car keys.
    - Take the ruler with you.
    - Put on a coat if it's cold. Else, just wear whatever you're already wearing.
    - Get in your car.
    - Start the car.
    - Drive to a store that sells drinking glasses.
    - Get out of the car.
    - Lock the car.
    - Enter the store.
- Pick and purchase a glass/glasses of suitable size.
    - Navigate yourself to the kitchenware section.
    - Find the section on the shelves that has drinking glasses.
    - Use the ruler to measure the diameter/width of the glasses on the shelf.
    - Stop measuring when you find a glass with an equal/greater width/diameter than "COOKIE"
    - If you measure a glass and it has an equal or greater diameter/width than "COOKIE", take that glass.
        - If the glass is not to your liking, put it back on the shelf.
        - Else, take the glass for purchase.
    - Else, put the glass back on the shelf and continue measuring the next glasses.
    - If you take a glass of sufficient width/diameter and it is to your liking, find your way to the checkout for purchase.
    - Buy the glass(es)
        - Greet the cashier
        - Give your glass(es) to the cashier so they can scan it/them.
        - Take your money out
        - Pay the appropriate amount (greater or equal to the price)
        - Take your purchased glass(es)
        - Thank the cashier
        - Say goodbye to the cashier
    
### How can this problem be solved with an app?

Create an app that calculates the required size of your raw cookie dough balls before they go in the oven, based on the width/diameter of your glass and the specific recipe that you use.
- Take the width/diameter of the glass
    - Create a designated space for users to enter that measurement into
    - Create a drop down menu next to that space that allows users to specify the unit of measurement used (cm, in, mm, etc.)
- Take the specific recipe used to make the cookies, entering the specific amount of each ingredient as well as any instructions that affect the size/density/firmness of the dough (eg. how the dough is mixed, how long the dough is mixed, if the dough has been chilled, how long the dough has been chilled, etc.)
    - Create a space where users can list the specific amounts of each ingredient in the recipe
        - Default to three blank ingredients listed.
        - Have an "add ingredient" option right below the list, so users can add any other ingredients.
        - Also have an option for users to delete ingredients from the list.
    - Next to each space, there should be drop down menus for specification.
        - One drop down menu should allow users to specify the amount of the ingredient used in the recipe.
        - Another should allow users to specify the type/variation of ingredient used in the recipe (eg. all purpose/pastry/whole wheat flour, medium/large eggs, soy/almond/dairy/rice milk, etc.)
    - Create another space where users can list any instructions that affect the size/density/firmness of the dough
        - There should be a space where the user can specify how the dough is mixed (eg. folded, beat, whisked, etc.)
        - Another space where the user can specify how long the dough is mixed.
        - Another space where the user can specify if/how long the dough is chilled.
- Take all these variables into consideration and calculate the approximate dimensions of the dough balls that would melt/expand/flatten into an ideal size for your drinking glass.
    - Calculate the required spherical dimensions of the ideal dough ball
    - Include tips on how the cookie may be affect if the dough ball is not spherical (if it is flattened, shaped, etc.)


## The spoon dropped into the gravy.

### How do you fix this problem?

Pick the spoon up and clean it.
- Pick the spoon up from the gravy
    - Use your dominant hand and take the spoon up from the gravy into the air
    - Be careful not to get gravy on your own hands to prevent unecessary mess
        - Do so by minimizing the number of fingers you use to pick the spoon up
    - Do not drop the spoon back into the gravy or onto the table/floor
        - If you are sitting, keep the spoon suspended over the table to prevent gravy from dripping onto your pants
        - Else, still try to keep the spoon suspended over the table, though it is not as crucial in this case
- Wipe the gravy off of the spoon.
    - If there is a tissue box/paper towel roll/napkin within your reach, take one tissue/paper towel/napkin.
    - Else, scan the room for an extra spoon.
            - If there is no extra spoon, set the dirty spoon back down into the gravy container with the handle resting on the container's rim. It is now someone else's problem.
            - Else, if there is an extra spoon, exchange the dirty spoon for the clean one.
    - With your tissue/paper towel/napkin, carefully wipe the spoon clean from the gravy.
        - Avoid touching the gravy with your bare skin.
        - Wipe the gravy off from one end to the other and wrap the excess gravy in the tissue/paper towel/napkin to contain it.

### How can you prevent this problem?

Place and replace the spoon somewhere outside of the container.


    (Tip: focus on steps, pick one way of doing things and break down the steps, doesn't have to be practical, just functional)
