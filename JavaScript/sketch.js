const model_url =
  'https://cdn.jsdelivr.net/gh/ml5js/ml5-data-and-models/models/pitch-detection/crepe/';
let pitch;

console.log("hey");

function setup() {
	audioContext = getAudioContext();
	mic = new p5.AudioIn(); //call constructor to create new object
	mic.start(listening);
}

function listening() {
  console.log('listening');
  pitch = ml5.pitchDetection(model_url, audioContext, mic.stream, modelLoaded);
}

function modelLoaded() {
	console.log("model loaded");
	pitch.getPitch(gotPitch);
}

function gotPitch(err, frequency) {
	if (err) {
		console.error(err);
	} else {
	console.log(frequency);
	}
	pitch.getPitch(gotPitch);
}


function draw() {
	background(220);
}