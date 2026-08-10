
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        """
        Determine if Alice wins the square game with optimal play.
      
        Game rules: Players take turns removing a perfect square number of stones.
        The player who removes the last stone wins.
      
        Args:
            n: Number of stones initially in the pile
          
        Returns:
            True if Alice (first player) wins, False otherwise
        """
        from functools import cache
      
        @cache
        def can_win(remaining_stones: int) -> bool:
            """
            Check if the current player can win from this game state.
          
            Args:
                remaining_stones: Number of stones left in the pile
              
            Returns:
                True if current player can force a win, False otherwise
            """
            # Base case: no stones left means previous player took the last stone
            if remaining_stones == 0:
                return False
          
            # Try all possible moves (removing perfect square number of stones)
            square_root = 1
            while square_root * square_root <= remaining_stones:
                stones_to_remove = square_root * square_root
              
                # If opponent cannot win after our move, then we can win
                if not can_win(remaining_stones - stones_to_remove):
                    return True
                  
                square_root += 1
          
            # No winning move found
            return False
      
        # Alice starts first, check if she can win
        return can_win(n)