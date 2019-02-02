<?php

 
/* Connect to mySQL database */  
$link = mysqli_connect("127.0.0.1",
    "quinterestdb", "quinterestdb",
    "quinterestdb");

/* Get input data */
$amount = $_GET['amount'];
mysqli_real_escape_string($link, $amount);
$tossupAmount = $amount;
$bonusAmount = $amount;
$sub = $_GET['sub'];
mysqli_real_escape_string($link, $sub);
$qtype = $_GET['qtype'];
mysqli_real_escape_string($link, $qtype);
$cat = $_GET ['categ'];
mysqli_real_escape_string($link, $cat);
$dif = $_GET['difficulty'];
mysqli_real_escape_string($link, $dif);
$tournamentyear = $_GET ['tournamentyear'];
mysqli_real_escape_string($link, $tournamentyear);

/* Check question type */
$tossup = FALSE;
$bonus = FALSE;
$qtype = $_GET ['qtype']; // Get Question Type
if ($qtype == "TossupBonus") {
    $tossup = TRUE;
    $bonus = TRUE;
} else if ($qtype == "Tossups") {
    $tossup = TRUE;
} else {
    $bonus = TRUE;
}

/* Check category */
if($cat=="All") {
	$categquery = "";
} else {
	$categquery = "AND Category = '$cat'";
}

if ($sub == "None" || $sub == "All") {
	$subcategquery = "";
} else {
	$subcategquery = "AND Subcategory = '$sub'";
}

/* Check difficulty */
if($dif=="All") {
	$difquery = "";
} else {
	$difquery = "AND Difficulty = '$dif'";
}

/* Check Tournament and Year */
if ($tournamentyear == "All") {
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
if ($tossup) {

    /* Open results div */
    echo "
        <div class='row'>
            <div class='col-md-12'>
                <center>
    ";

	/* Run Query */
	$query ="SELECT * FROM tossupsdbnew WHERE ID LIKE '%%%%' $categquery $subcategquery $difquery $tournamentquery";
    $getQuery = mysqli_query($link, $query);
    
    if ($getQuery == FALSE) {
        $resultsSize = 0;

        echo "<p>Sorry, there are no matching tossups.</p>";
    } else {
        $resultsSize = mysqli_num_rows($getQuery);
        
        /* Displaying the number of results */
        if ($resultsSize > $tossupAmount) {
            echo "<p>$tossupAmount Random Tossups Were Found That Match Your Search Settings</p>";
        } else {
            echo "<p>$resultsSize Random Tossups Were Found That Match Your Search Settings</p>";
            $tossupAmount = $resultsSize; // If resultsSize is smaller, change amount.
        }
    }

    /* Close results div */
    echo "
                </center>
            </div>
        </div>
        <hr>
    ";

    /* Looping through and returning results */
    $resultsCounter = 1;
    $offsets = array();
    while ($resultsCounter <= $tossupAmount) {

        /* Getting an unused offset */
        $offset = rand(0, $resultsSize);
        while (in_array($offset, $offsets)) {
            $offset = rand(0, $resultsSize);
        }
        $offsets[$resultsCounter - 1] = $offset;


        $singleResult = $query . " LIMIT $offset, 1";
        $getQuery = mysqli_query($link, $singleResult);
        if ($getQuery != FALSE) {
            
            $row = mysqli_fetch_array($getQuery);
            
            $id = $row['ID'];
            $answer = stripslashes($row['Answer']);
            $category = $row['Category'];
            $subcategory = $row['Subcategory'];
            $num = $row['Question #'];
            $difficulty = $row['Difficulty'];
            $question = stripslashes($row['Question']);
            $round = $row['Round'];
            $tournament = $row['Tournament'];
            $year = $row['Year'];

            // What will be displayed on the results page 
            echo "
                <div class='row'>
                    <div class='col-md-12'>
                        <p><b>Result: $resultsCounter | $tournament | $year | $round | $num | $category | $subcategory</b><span style='float: right'>ID: $id</span></p>
                        <p><em>Question:</em> $question</p>
                        <p><em><strong>ANSWER:</strong></em> $answer</p>
                    </div> 
                </div>
                <hr>
            ";
        }

        $resultsCounter++;

    }
}

/***********************/
/* BONUS QUESTION TYPE */
/***********************/
if ($bonus) {

    /* Open results div */
    echo "
        <div class='row'>
            <div class='col-md-12'>
                <center>
    ";

    $query = "SELECT * FROM bonusesdb WHERE ID LIKE '%%%%' $categquery $subcategquery $difquery $tournamentquery"; //completed search query
    $getQuery = mysqli_query($link, $query);
    
    if ($getQuery == FALSE) {
        $resultsSize = 0;

        echo "<p>Sorry, there are no matching bonuses.</p>";
    } else {
        $resultsSize = mysqli_num_rows($getQuery);
        
        /* Displaying the number of results */
        if ($resultsSize > $bonusAmount) {
            echo "<p>$bonusAmount Random Bonuses Were Found That Match Your Search Settings</p>";
        } else {
            echo "<p>$resultsSize Random Bonuses Were Found That Match Your Search Settings</p>";
            $bonusAmount = $resultsSize; // If resultsSize is smaller, change amount.
        }
    }



    /* Close results div */
    echo "
                </center>
            </div>
        </div>
        <hr>
    ";

    /* Looping through and returning results */
    $resultsCounter = 1;
    $offsets = array();
    while ($resultsCounter <= $bonusAmount) {

        /* Getting an unused offset */
        $offset = rand(0, $resultsSize);
        while (in_array($offset, $offsets)) {
            $offset = rand(0, $resultsSize);
        }
        $offsets[$resultsCounter - 1] = $offset;

        $singleResult = $query . " LIMIT $offset, 1";
        $getQuery = mysqli_query($link, $singleResult);

        if ($getQuery != FALSE) {

            $row = mysqli_fetch_array($getQuery);

            $a1 = stripslashes($row['Answer1']);
            $a2 = stripslashes($row['Answer2']);
            $a3 = stripslashes($row['Answer3']);
            $category = $row['Category'];
            $subcategory = $row['Subcategory'];
            $num = $row['Question #'];
            $difficulty = $row['Difficulty'];
            $q1 = stripslashes($row['Question1']);
            $q2 = stripslashes($row['Question2']);
            $q3 = stripslashes($row['Question3']);
            $intro = stripslashes($row['Intro']);
            $round = $row['Round'];
            $tournament = $row['Tournament'];
            $year = $row['Year'];
            $id = $row['ID'];

            echo "<div class='row'>
                    <div class='col-md-12'>
                        <p><b>Result: $resultsCounter | $tournament |$year | $round | $num | $category | $subcategory | $difficulty</b><span style='float: right'>ID: $id</span>
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
        }
        $resultsCounter++;
    }
}

?>
