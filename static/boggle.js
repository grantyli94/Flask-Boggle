"use strict";

const $playedWords = $("#words");
const $form = $("#newWordForm");
const $wordInput = $("#wordInput");
const $message = $(".msg");
const $table = $("table");

const HEIGHT = 5;
const WIDTH = 5;

let gameId;


/** Start */

async function start() {
  let response = await axios.get("/api/new-game");
  gameId = response.data.gameId;
  let board = response.data.board;

  displayBoard(board);
}

/** Display board */

function displayBoard(board) {
  // $table.empty();
  for (y = 0; y < HEIGHT; y++) {
    $row = $("<tr>");
    for (x = 0; x < WIDTH; x++) {

    }
  }
  // loop over board and create the DOM tr/td structure
}


start();