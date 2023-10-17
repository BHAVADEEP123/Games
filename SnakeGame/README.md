There are 2 objects that will created 
    1) snake with initial size of 3 which is declared in constants file
        -> It is created only in the start
    2) food with some size declared in the constants file
        -> It is created in the start
        -> also a new food object will be created when ever snake eats one with old one getting deleted.

There is a window.mainloop() function called which runs in background, which waits for inputs from mouse or keyboard.

And in the next_turn() method we invoke method.after(*)
which does the following waits for 1st parameter milliseconds and then invokes the second parameter with arguments being from 3rd parameter
    eg: window.after(delay_in_milliseconds, function_name, *args)

So our game runs in this next_turn which runs until there is a collision to the wall or snake itself.
and direction changes when we press <up>,<down>,<left>,<right> buttons. (which are invoked by the .mainloop method)

IMP: when next_turn is invoked then the we attach a snake box in front of the existing snake and delete the last ones.