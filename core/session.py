import random

class Session:
    PHASE_FORWARD = "forward"
    PHASE_REVERSE = "reverse"
    MAX_STAGE = 14
    MIN_STAGE = 0
    CORRECT_TO_ADVANCE = 1
    WRONG_TO_REDUCE = 1

    def __init__(self, input_module):
        self.phase = self.PHASE_FORWARD
        self.input_module = input_module
        self.stage = 7
        self.correct_count = 0
        self.wrong_count = 0
        self.finished = False
        self.last_correct = None
        self.sign_direction = None

    def update(self):
        print(f"[DEBUG] stage={self.stage}, phase={self.phase}")
        self.sign_direction = random.randint(0, 3)

    def answer(self, direction):
        if direction == -1 :
            print("語音辨識錯誤 請在試一次")
            return
        self.last_correct = (direction == self.sign_direction)
        print(f"[DEBUG] user_input={direction}, correct={self.last_correct}")

        if self.phase == self.PHASE_FORWARD:
            if self.last_correct:
                self.correct_count += 1
                self.wrong_count = 0
                if self.correct_count >= self.CORRECT_TO_ADVANCE:
                    self.stage += 1
                    self.correct_count = 0
            else:
                self.wrong_count += 1
                self.correct_count = 0
                if self.wrong_count >= self.WRONG_TO_REDUCE:
                    self.phase = self.PHASE_REVERSE
                    self.correct_count = 0
                    self.wrong_count = 0

        elif self.phase == self.PHASE_REVERSE:
            if self.last_correct:
                self.correct_count += 1
                self.wrong_count = 0
                if self.correct_count >= 1:
                    self.finished = True
            else:
                self.wrong_count += 1
                self.correct_count = 0
                if self.wrong_count >= 2:
                    self.stage -= 1
                    self.correct_count = 0
                    self.wrong_count = 0

        if self.stage < self.MIN_STAGE:
            self.stage = self.MIN_STAGE
            self.finished = True
        elif self.stage > self.MAX_STAGE:
            self.stage = self.MAX_STAGE
            self.finished = True

    # def get_result(self):
    #     stage = max(self.MIN_STAGE, min(self.stage, self.MAX_STAGE))
    #     acuity_score = 5.3 - 0.1 * (self.MAX_STAGE - stage)
    #     return round(acuity_score, 1)
