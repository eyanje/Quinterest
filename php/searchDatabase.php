<?php

/* Connecting to mySQL database */
$link = mysqli_connect("127.0.0.1",
    "quinterestdb", "quinterestdb",
    "quinterestdb");

$tossup = FALSE;
$bonus = FALSE;

/* Get Inputs */
$qtype = $_GET ['qtype'];
mysqli_real_escape_string($link, $qtype);

$cat = $_GET['categ'];
mysqli_real_escape_string($link, $cat);

$sub = $_GET['sub'];
mysqli_real_escape_string($link, $sub);

$dif = $_GET['difficulty'];
mysqli_real_escape_string($link, $dif);

$tournamentyear = $_GET['tournamentyear'];
mysqli_real_escape_string($link, $tournamentyear);

$search = stripslashes($_GET['info']);
mysqli_real_escape_string($link, $search);
$search_exploded = explode(" ", $search);

$stype = $_GET['stype'];
mysqli_real_escape_string($link, $stype);

$limit = $_GET['limit'] == "yes";

/* Get Question Type */
if ($qtype == "TossupBonus") {
    $tossup = TRUE;
    $bonus = TRUE;
} else if ($qtype == "Tossups") {
    $tossup = TRUE;
} else {
    $bonus = TRUE;
}

/* Check Category */
if ($cat == "All") {
    $categquery = "";
} else {
    $categquery = "AND Category = '$cat'";
}

/* Check Subcategory */
if( $sub=="None" || $sub=="All") {
    $subcategquery = "";
} else {
    $subcategquery = "AND Subcategory = '$sub'";
}

/* Check Difficulty */
if( $dif == "All") {
    $difquery = "";
} else {
    $difquery = "AND Difficulty = '$dif'";
}

/* Check Tournament and Year */
if($tournamentyear == "All") {
    $tournamentquery = "";
} else {
    $explode = explode(',', $tournamentyear);
    $tvalue = $explode[0];
    $yvalue = $explode[1];
    $tournamentquery = "AND (Tournament = '$tvalue' AND Year = '$yvalue')";
}

/************************/
/* TOSSUP QUESTION TYPE */
/************************/
if ($tossup == true) {

    /* Constructing Query */
    $construct = "";
    $x = 0;
    foreach ($search_exploded as $search_each) { //loops through array
        $x++;
        if($x == 1) {
            $construct .='(Answer COLLATE utf8_general_ci LIKE _utf8"%' . $search_each . '%" COLLATE utf8_general_ci)'; //if only one value in array
        } else {
            $construct .='AND (Answer COLLATE utf8_general_ci LIKE _utf8"%' . $search_each . '%" COLLATE utf8_general_ci)'; //for each multiple value in array
        }
    }
    if($stype == "AnswerQuestion") {
        $construct .='OR (Question COLLATE utf8_general_ci LIKE _utf8"%' . $search . '%" COLLATE utf8_general_ci)';
    }
    $constructs = "SELECT * FROM tossupsdbnew WHERE ($construct) $categquery $subcategquery $difquery $tournamentquery ORDER BY `Year` DESC,`Tournament` ASC,`Round` ASC,`Question #` ASC";

    if ($limit == TRUE) {
        /* Querying the database */
        $getquery = mysqli_query($link, $constructs);

        
        /* Display Number of Results */
        echo "
            <div id='tossupResults'>
                <div class='row'>
                    <div class='col-md-12'>
                        <center>
        ";

        if ($getquery == FALSE) {
            echo "<p>Sorry, there are no matching tossups.</p>";
        } else {
            $foundnum = mysqli_num_rows($getquery);
            $getquery = mysqli_query($link, $constructs . " LIMIT 10");
        
            echo "<p>$foundnum Tossups Were Found</p>";

        }

        echo "
            </center></div></div><hr>
        ";
    } else {
        $getquery = mysqli_query($link, $constructs . " LIMIT 10, 18446744073709551615"); // Skips First 10 Rows
    }
    
    if ($getquery != FALSE) {
        /* Displaying Results */ 
        if ($limit) {
            $a = 1;
        } else {
            $a = 11;
        }

        while ($runrows = mysqli_fetch_array($getquery)) { // Fetching results
            $id = $runrows['ID'];
            $answer = stripslashes($runrows['Answer']);
            $category = $runrows['Category'];
            $subcategory = $runrows['Subcategory'];
            $num = $runrows['Question #'];
            $difficulty = $runrows['Difficulty'];
            $question = stripslashes($runrows['Question']);
            $round = $runrows['Round'];
            $tournament = $runrows['Tournament'];
            $year = $runrows['Year'];

            // What will be displayed on the results page 
            echo "
                <div class='row'>
                    <div class='col-md-12'>
                        <p><b>Result: $a | $tournament | $year | Round: $round | Question: $num | $category | $subcategory</b><span style='float: right'>ID: $id</span></p>
                        <p><em>Question:</em> $question</p>
                        <p><em><strong>ANSWER:</strong></em> $answer</p>
                    </div> 
                </div>
                <hr>
            ";
            $a++;
        }

        if ($limit) {
            if ($foundnum > 10) {
                echo "
                <div id='loadAllTossups'>
                    <div class='row'>
                        <div class='col-md-12'>
                            <center>
                            <button type='button' id='loadAllTossupsButton' class='btn btn-lg btn-primary'>Load All Tossups</button>
                            </center>
                        </div>
                    </div>
                    <hr>
                </div>
                ";
            }
            echo "</div> <!-- Closing tossupResults -->";
        }
    }
}

/***********************/
/* BONUS QUESTION TYPE */
/***********************/
if ($bonus) {

    /* Constructing Bonus Query */
    $construct = "";   
    $x = 1;
    foreach ($search_exploded as $search_each) {
        if ($x == 1) {
            $construct .='((Answer1 COLLATE utf8_general_ci LIKE _utf8"%' . $search_each . '%" COLLATE utf8_general_ci)';
        } else {
            $construct .=' AND (Answer1 COLLATE utf8_general_ci LIKE _utf8"%' . $search_each . '%" COLLATE utf8_general_ci)';
        }
        $x++;
    }
    $construct .=")";

    $x = 1;
    foreach($search_exploded as $search_each) {
        if($x==1) {
            $construct .='OR ((Answer2 COLLATE utf8_general_ci LIKE _utf8"%' . $search_each . '%" COLLATE utf8_general_ci)';
        } else {
            $construct .=' AND (Answer2 COLLATE utf8_general_ci LIKE _utf8"%' . $search_each . '%" COLLATE utf8_general_ci)';
        }
        $x++;
    }
    $construct .=")";

    $x = 1;
    foreach($search_exploded as $search_each) {
        if($x==1) {
            $construct .='OR ((Answer3 COLLATE utf8_general_ci LIKE _utf8"%' . $search_each . '%" COLLATE utf8_general_ci)';
        } else {
            $construct .=' AND (Answer3 COLLATE utf8_general_ci LIKE _utf8"%' . $search_each . '%" COLLATE utf8_general_ci)';
        }
        $x++;
    }
    $construct .=")";

    if($stype == "AnswerQuestion") {

        $x = 1;
        foreach($search_exploded as $search_each) {
            if($x == 1) {
                $construct .='OR ((Question1 COLLATE utf8_general_ci LIKE _utf8"%' . $search_each . '%" COLLATE utf8_general_ci)';
            } else {
                $construct .='AND (Question1 COLLATE utf8_general_ci LIKE _utf8"%' . $search_each . '%" COLLATE utf8_general_ci)';
            }
            $x++;
        }
        $construct .= ")";

        $x = 1;
        foreach($search_exploded as $search_each) {
            if($x == 1) {
                $construct .='OR ((Question2 COLLATE utf8_general_ci LIKE _utf8"%' . $search_each . '%" COLLATE utf8_general_ci)';
            } else {
                $construct .='AND (Question2 COLLATE utf8_general_ci LIKE _utf8"%' . $search_each . '%" COLLATE utf8_general_ci)'; 
            }
            $x++;
        }
        $construct .= ")";

        $x = 1;
        foreach($search_exploded as $search_each) {
            if($x == 1) {
                $construct .= 'OR ((Question3 COLLATE utf8_general_ci LIKE _utf8"%' . $search_each . '%" COLLATE utf8_general_ci)';
            } else {
                $construct .= 'AND (Question3 COLLATE utf8_general_ci LIKE _utf8"%' . $search_each . '%" COLLATE utf8_general_ci)'; 
            }
            $x++;
        }
        $construct .= ")";

        $construct .= 'OR Intro COLLATE utf8_general_ci LIKE _utf8"%' . $search . '%" COLLATE utf8_general_ci';
    }

    $constructs = "SELECT * FROM bonusesdb WHERE ($construct) $categquery $subcategquery $difquery $tournamentquery ORDER BY `Year` DESC,`Tournament` ASC,`Round` ASC,`Question #` ASC";
    
    if ($limit) {
        /* Query the Database */
        $getquery = mysqli_query($link, $constructs);
    
        /* Display Results */
        echo "
            <div id='bonusResults'>
                <div class='row'>
                    <div class='col-md-12'>
                        <center>
        ";

        if ($getquery == FALSE) {
            echo "<p>Sorry, there are no matching bonuses.</p>";
        } else {
            $foundnum = mysqli_num_rows($getquery);
            
            /* Only use the first 10 bonuses */
            $getquery = mysqli_query($link, $constructs . " LIMIT 10");

            echo "<p>$foundnum bonuses Were Found</p>";
        }
        
        echo "
            </center></div></div><hr>
        ";

    } else {
        $getquery = mysqli_query($link, $constructs . " LIMIT 10, 18446744073709551615"); // Skips First 10 Rows
    }
  
    if ($getquery != FALSE) {
        /* Displaying Results */ 
        if ($limit) {     
            $a = 1;
        } else {
            $a = 11;
        }
        while ($runrows = mysqli_fetch_array($getquery)) {
            $a1 = stripslashes($runrows['Answer1']);
            $a2 = stripslashes($runrows['Answer2']);
            $a3 = stripslashes($runrows['Answer3']);
            $category = $runrows['Category'];
            $subcategory = $runrows['Subcategory'];
            $num = $runrows['Question #'];
            $difficulty = $runrows['Difficulty'];
            $q1 = stripslashes($runrows['Question1']);
            $q2 = stripslashes($runrows['Question2']);
            $q3 = stripslashes($runrows['Question3']);
            $intro = stripslashes($runrows ['Intro']);
            $round = $runrows ['Round'];
            $tournament = $runrows ['Tournament'];
            $year = $runrows ['Year'];
            $id = $runrows ['ID'];

            echo "<div class='row'>
                    <div class='col-md-12'>
                        <p><b>Result: $a | $tournament |$year | $round | $num | $category | $subcategory | $difficulty</b><span style='float: right'>ID: $id</span>
                        <p><em>Question:</em> $intro </p>
                        <p><strong>[10]</strong> $q1</p>
                        <p><em><strong>ANSWER:</strong></em> $a1</p>
                        <p><strong>[10]</strong> $q2</p>
                        <p><em><strong>ANSWER:</strong></em> $a2</p>
                        <p><strong>[10]</strong> $q3</p>
                        <p><em><strong>ANSWER:</strong></em> $a3</p>
                    </div>
                </div><hr>
            ";
            $a++;
        }
    }

    if ($limit) {
        if ($getquery != FALsE) {
            if ($foundnum > 10) {
                echo "
                    <div id='loadAllBonuses'>
                        <div class='row'>
                            <div class='col-md-12'>
                                <center>
                                <button type='button' id='loadAllBonusesButton' class='btn btn-lg btn-primary'>Load All Bonuses</button>
                                </center>
                            </div>
                        </div>
                        <hr>
                    </div>
                ";
            }
            echo "</div> <!-- Closing bonusResults -->";
        }
    }
}
?>
