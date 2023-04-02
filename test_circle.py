

import unittest

import pygame

import circle


class MovableCircleTest(unittest.TestCase):
    def test_when_circle_starts_then_running_is_OK(self):
        c = circle.MovableCircle()
        self.assertEqual(c.running, True)
        c.stop()

    def test_when_circle_runs_then_pressing_q_stops_running(self):
        c = circle.MovableCircle()
        pygame.key.get_pressed = self.create_key_mock(pygame.K_q)
        c.run()
        self.assertEqual(c.running, False)

    def create_key_mock(self, pressed_key):
        def helper():
            tmp = [0] * 300
            tmp[pressed_key] = 1
            return tmp
        return helper
 

if __name__ == '__main__':
    unittest.main()

