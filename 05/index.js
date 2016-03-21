var data  = [-1,7,8,7,1,-2,-1,11,3,2,4,-2,-1,50,0,0,0,-2,-1,14,6,7,1,-2,-1,36,13,1,0,-2,-1,11,12,5,0,-2,-1,16,14,9,0,-2,-1,40,18,14,0,-2,-1,22,4,8,8,-2,-1,8,13,17,0,-2,-1,13,15,12,0,-2,-1,33,16,9,0,-2,-1,48,104,3,0,-2,-1,8,0,0,8,-2,-1,17,8,16,5,-2,-1,9,24,6,1,-2,-1,17,15,7,7,-2,-1,18,18,5,0,-2,-1,9,12,0,2,-2,-1,0,0,23,0,-2,-1,11,7,1,0,-2,-1,12,20,0,0,-2,-1,25,17,0,17,-2,-1,24,13,0,0,-2,-1,0,0,10,9,-2,-1,1,9,1,0,-2,-1,99,0,0,0,-2,-1,51,9,0,5,-2,-1,25,5,0,0,-2,-1,29,27,6,9,-2,-1,9,0,0,0,-2,-1,0,0,0,66,-2,-1,0,0,0,0,-2,-1,0,0,0,0,-2,-1,0,0,0,0,-2,-1,0,0,0,0,-2,-1,0,0,0,0,-2,-1,0,0,0,0,-2,-1,0,0,0,0,-2,-1,0,0,0,0,-2,-1,0,0,0,0,-2,-1,0,0,0,0,-2,-1,0,0,0,0,-2,-1,0,0,0,0,-2,-1,0,0,0,0,-2,-1,0,0,0,0,-2,-1,0,0,0,0,-2,-1,0,0,0,0,-2,-1,0,0,0,0,-2,-1,0,0,0,0,-2,-1,0,0,0,0,-2,-1,0,0,0,0,-2,-1,0,0,0,0,-2,-1,0,0,0,0,-2,-1,0,0,0,0,-2];
var count = 0;
var states=-1;
var s = ["Iowa", "New Hampshire", "South Carolina", "Nevada", "Alabama", "Alaska", "Arkansas", "Georgia", "Massachusetts", "Minnesota", "Oklahoma", "Tennessee", "Texas", "Vermont", "Virginia", "Kansas", "Kentucky", "Louisiana", "Maine", "Puerto Rico", "Hawaii", "Idaho", "Michigan", "Mississippi", "District of Columbia", "Wyoming", "Florida", "Illinois", "Missouri", "North Carolina", "Northern Marina Islands", "Ohio", "Colorado", "Virgin Islands", "American Samoa", "Arizona", "Utah", "Dakota", "Wisconsin", "New York", "Connecticut", "Delaware", "Maryland", "Pennsylvania", "Rhode Island", "Indiana", "Nebraska", "West Virginia", "Oregon", "Washington", "California", "Montana", "New Jersey", "New Mexico", "South Dakota"]

d3.select(".chart")
  .selectAll("div")
    .data(data)
  .enter().append("div")
    .style("width", function(d) {
      if(d!=-1){
        if(d==0){
          return "5px";
        }
        return d*7 + "px";
      }
      else{
        return "100px";
      }
    })
    .style("display", function(){
      if(count<=5){
        //console.log(count);
        if(count==5){
          //console.log(count);
          count = 0;
          return "block";
        } else{
          //console.log(count);
          count++;
          //console.log("here");
          return "inline-block";
        }
      }
    })
    .style("visibility", function(d){
      if(d==-2){
        return "hidden";
      }
    })
    .style("margin-right", function(){
      return "-1px";
    })
    
    .style("background-color", function(d){
      if(d==-1 || d==-2){
        return "#FFFFFF";
      } console.log(count);
      if(count<=3){
        if(count==3){
          count=0;
          return "#FE9898";
        } else if(count==2){
          count++;
          return "#D86161";
        } else if(count==1){
          count++;
          return "#B23535";
        } else if(count==0){
          count++;
          return "#8C1515";
        }
      }
    })
    
    .style("color", function(d){
      if(d==-1 || d==-2){
        return "#262626";
      }
    })
    .style("text-align", function(d){
      if(d==-1){
        return "left";
      }
    })
    .text(function(d) {
      //console.log(d + ", " + count);
      if(d>=0){
        return d;
      } else if(d==-1){
        states++;
        return s[states];
      }
    });