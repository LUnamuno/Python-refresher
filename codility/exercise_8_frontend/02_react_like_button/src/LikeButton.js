import React, { useState } from 'react';
import classNames from 'classnames';

const INITIAL_LIKES = 100;

export default function LikeButton() {
  const [likes, setLikes] = useState(INITIAL_LIKES);
  const [liked, setLiked] = useState(false);

  const handleClick = () => {
    // A click toggles the like: +1 when adding it, -1 when undoing it.
    setLikes((current) => (liked ? current - 1 : current + 1));
    setLiked((current) => !current);
  };

  return (
    <button
      className={classNames('like-button', { liked })}
      onClick={handleClick}
    >
      Like | <span className="likes-counter">{likes}</span>
    </button>
  );
}
