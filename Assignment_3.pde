// CPSC 583 assignment 3
// Introduction to Processing
// Seongmok, Yoo (Eric)
// 10162624


// initial setup with frame size and white backgournd
void setup(){   
  size(500,500);
  background(255,255,255);
}

// calling draw function to create visualization
void draw(){
    // create a line following the current mouse position
   line(mouseX,mouseY, pmouseX,pmouseY);
   
   //conditional using keyPressed boolean variable    // Use ASCII code to check if the key is alphanumeric
   // part of the code used from: https://www.michellechandra.com/processing/generative-art/
   if (keyPressed == true){
     // check if pressed key is a letter
     // if yes, draw rectangle in random position
     if (key >= 65 && key <= 122) {
       float x = random(0,500);
       float y = random(0,500);
       rect(x,y,100,50); 
     
     // if pressed key is not a letter, reset the visualization
     } else { 
       background(255,255,255);
     } 
   }  

   
   // if mouse is pressed, draw ellipse following the mouse    
   if (mousePressed == true){
     //call strokeEllipse
     strokeEllipse(mouseX, mouseY, pmouseX, pmouseY);
     
   }
   // if mouse is not pressed, draw a line following the mouse
   else{
     line(mouseX,mouseY, pmouseX,pmouseY);
     
   }
}

// function called to draw ellipses which changes its size depending on the speed of the mouse
// part of the code used from: https://processing.org/examples/pattern.html
void strokeEllipse(int x, int y, int px, int py) {
  float speed = abs(x-px) + abs(y-py);
  stroke(speed);
  ellipse(x, y, speed, speed);
}

// function called to draw rectangles which changes its size depending on the speed of the mouse
// part of the code used from: https://processing.org/examples/pattern.html
void strokeRect(int x, int y, int px, int py) {
  float speed = abs(x-px) + abs(y-py);
  stroke(speed);
  ellipse(x, y, speed, speed);
}
