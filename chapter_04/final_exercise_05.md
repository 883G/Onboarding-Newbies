# Final Exercise 05 - Spark RDD Exercises with Joker and Batman :black_joker: :bat:

## Overview
Welcome to the Spark RDD Exercises with a Joker and Batman twist! In this exercise session, you will tackle various Spark RDD. These exercises will help you sharpen your skills in Spark's core data structure and processing model. RDDs are your trusted allies in the world of Spark, and mastering them is essential for conquering big data challenges.

:warning: **How to setup Spark Cluster?**
- For this exercise, you will need to setup a Spark Cluster. You can use the [Databricks Community Edition](https://community.cloud.databricks.com/login.html) for this exercise, use the free version for 14 days, it's enough for this exercise. (we hope so... :smile:)
after the first page of sign up click on "Get started with community edition"
<img width="200" alt="image" src="https://github.com/883G/Onboarding-Newbies/assets/60566128/fd517a13-d3d3-48fe-9295-fa7fd6308d0e">
 

## Exercise 1: The Joker's Challenge - Calculate Factorial
The Joker has a mathematical puzzle for you! Write a Spark program that receives a number `N` and returns its factorial. Can you solve the Joker's riddle?

## Exercise 2: Batman's Mission - Filter and Sort Numbers
Batman is on a mission to clean up Gotham City. Write a Spark program that receives four integers `X1`, `X2`, `Y1`, and `Y2`. Your mission, should you choose to accept it:
   - Find all the numbers between `X1` and `X2` that can be divided by 3.
   - Find all the numbers between `Y1` and `Y2` that can be divided by 4.
   - Remove any criminal duplicates.
   - Sort the numbers in ascending order and restore peace to the city.

## Exercise 3: Joker's Mischief - Count Email Addresses
The Joker is causing chaos with spam emails! Write a Spark program that loads files from [./dataset/fake_spam_dataset.csv](./dataset/fake_spam_dataset.csv) and prints how many email addresses there are in the files for each email provider. The Joker is trying to trick you with his spam emails. Can you foil his plans?

## Exercise 4: The Battle of Broadcast - Find Common Soldier Names
In the dark and chaotic streets of Gotham City, the Joker is hatching a sinister plan to create chaos and confusion. He has enlisted his loyal henchmen, known as the "Joker's Henchclowns," while Batman has gathered his trusted allies, known as the "Gotham Protectors."

Your mission, should you choose to accept it, is to uncover the spies who secretly serve both the Joker and Batman. You have two lists: one containing the names of the Joker's Henchclowns and the other containing the names of the Gotham Protectors. Your task is to identify the double agents who appear on both lists.
Use the file [./dataset/joker_henchclowns.csv](./dataset/jokers_henchclowns.csv) to create an RDD of the Joker's Henchclowns. Use the file [./dataset/gotham_protectors.csv](./dataset/gotham_protectors.csv) to create an RDD of the Gotham Protectors.

To achieve this mission and save Gotham City from impending chaos, you must harness the power of broadcast variables. Make a strategic decision about which side to broadcast and why. The fate of Gotham hangs in the balance, and only you can thwart the Joker's sinister plan!

Good luck, detective!

## Exercise 5: Batman's Data Detective - Count Different HTTP Request Types
Batman needs your help to investigate the Joker's online activities! Analyze a log file of HTTP requests to Israelies news websiters located at [./dataset/access.log](./dataset/access.log). Your task is to find out how many different types of HTTP requests the Joker has made in the log file. Batman has provided you with an accumulator to tally the results. Can you bring the Joker to justice?

## Exercise 6: Gotham City Crime Decryption: A Spark-Powered Bat-Adventure :bat: :night_with_stars: :detective:

### a. Deciphering the Batcomputer's Data
- Access the Batcomputer and load the [gotham_crimes_crime.csv](./dataset/gotham_crime_data.csv) file into a Spark DataFrame.
- Reveal the structure of Gotham's crime data by displaying the DataFrame's schema.

### b. When Does the Joker Laugh? Analyzing Crime by Day
- Determine the day of the week (`CrimeDayOfWeek`) when Gotham's arch-villains, like the Joker, are most active.

### c. The Riddler's Monthly Riddles: Crime Pattern Analysis
- Unravel the Riddler's riddles by finding out in which month (`CrimeMonth`) Gotham faces the highest crime spree.

### d. Missing Citizens of Gotham: The Search for the Lost
- Batman's list: Identify all cases where the `CrimeCategory` is 'MISSING PERSON' and yet to be solved (`CrimeResolution` not 'FOUND PERSON').
- Highlight the plight of Gotham's missing souls, still waiting to be found.

### e. The Penguin's Turf: Unresolved Crimes in Gotham’s Alleys
- Dive into Gotham's dark alleys and identify the top 3 `CrimeCategory` with unresolved cases (`'UNRESOLVED'`) for each unique `Address`.
- Use your detective skills with DataFrame operations to map out the Penguin’s crime territories and patterns.

### f. Preserving Gotham’s Data: Saving to the Batcomputer’s Database
- Save all the DataFrame data into the DBFS (Databricks File System) using the Parquet Format with SNAPPY compression, partitioned by `CrimeDate` (`DT`).

### g. Batcomputer Analysis: Assessing Data Storage
i. Investigate how many files (parts) were created under the directory after saving the data.
ii. Develop a program that ensures only one file is saved to the DBFS. Compare different methods to accomplish this.
1) Discover an alternative way to save only one file.
2) Discuss the differences between the methods used for saving the data.

### h. Tracking Crime Time: Analyzing the Most and Least Active Hours
- Analyze the crime data to determine which hour of the day witnessed the most crimes and which had the least.
- Provide insights to Batman, so he can strategize his patrol hours more effectively.

## Instructions
- Use only Spark DataFrame operations for Gotham City Crime Analysis exercises.
- Employ RDD operations and performance techniques for Joker and Batman exercises.
- Use Python for all exercises.
- Give at least one solution with 2 way to solve the problem, one more efficient than the other.
- Embrace performance optimization techniques like broadcast variables and accumulators when applicable.
- Document your code clearly, just as Batman keeps records of his battles.
- Feel free to consult the Spark documentation and resources for guidance.
- You can find the dataset for the exercises in the [./dataset](./dataset) folder.
- Write your code in solution files named `solution_01.py`, `solution_02.py`, etc.

Join Batman in his quest for justice and outsmart the Joker with your Spark skills!
