class Head:
    def __init__(self, ears, eyes, mouth, nose):
        self.ears = ears
        self.eyes = eyes
        self.mouth = mouth
        self.nose = nose
        print("Head created successfully")


class Torso:
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg
        print("Torso created successfully")


class Arm:
    def __init__(self, right_hand, left_hand):
        self.right_hand = right_hand
        self.left_hand = left_hand
        print("Arms created successfully")  


class Hand:
    def __init__(self, fingers):
        self.fingers = fingers
        print("hand created successfully")

class Leg:
    def __init__(self, right_foot, left_foot):
        self.right_foot = right_foot
        self.left_foot = left_foot
        print("Legs created successfully")

class Foot:
    def __init__(self, toes):
        self.toes = toes
        print("Foot created successfully")

class Human:
    def __init__(self, head, torso, arm, hand, leg, foot):
        self.head = head
        self.torso = torso
        self.arm = arm
        self.hand = hand
        self.leg = leg
        self.foot = foot
        print("Human created successfully")


right_hand = Hand(5)
left_hand = Hand(5)
right_foot = Foot(5)
left_foot = Foot(5)

arm = Arm(right_hand, left_hand)
leg = Leg(right_foot, left_foot)
head = Head(2, 2, 1, 1)

torso = Torso(head, leg, arm, leg, leg)
