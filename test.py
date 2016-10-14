import pygame

import serge.engine
import serge.actor
import serge.blocks.visualblocks
import serge.blocks.utils
import serge.blocks.directions

class Snake(serge.actor.CompositeActor):
    """Represents the snake"""

    def __init__(self):
        """Initialise the snake"""
        super(Snake, self).__init__('snake', 'snake-head')
        self.visual = serge.blocks.visualblocks.Circle(16, (0,255,0))
        self.setLayerName('middle')
        self.current_direction = serge.blocks.directions.N

    def addedToWorld(self, world):
        """The snake was added to the world"""
        super(Snake, self).addedToWorld(world)
        #
        self.keyboard = serge.engine.CurrentEngine().getKeyboard()

    def updateActor(self, interval, world):
        """Update the snake"""
        super(Snake, self).updateActor(interval, world)
        #
        # Move the head
        if self.keyboard.isClicked(pygame.K_LEFT):
            rotation = +90
        elif self.keyboard.isClicked(pygame.K_RIGHT):
            rotation = -90
        else:
            rotation = 0
        #
        # Change direction
        if rotation:
            current_angle = serge.blocks.directions.getAngleFromCardinal(self.current_direction)
            self.current_direction = serge.blocks.directions.getCardinalFromAngle(current_angle+rotation)
        #
        # Move
        offset = 5*serge.blocks.directions.getVectorFromCardinal(self.current_direction)
        self.move(*offset)
        #
        # Add a new segment if needed
        if not self.getChildren() or self.getDistanceFrom(self.getChildren()[-1]) > 16:
            self.addSegment()

    def addSegment(self):
        """Add a new body segment"""
        segment = serge.actor.Actor('segment')
        segment.visual = serge.blocks.visualblocks.Circle(16, (0,200,0))
        segment.setLayerName('middle')
        segment.moveTo(self.x, self.y)
        self.addChild(segment)


# Create the engine
engine = serge.blocks.utils.getSimpleSetup(800, 600)
world = engine.getWorld('lab')

# Create the snake
snake = Snake()
world.addActor(snake)
snake.moveTo(400, 300)

# Run the game
engine.run(60)