// Component for About Me
// Will give basic information about me (the developer of this website) and a chance to support me

import {Link} from 'react-router-dom'

const AboutMeToolbar = () => {
	return (
		<header>
			<div className="container2">
				<Link to="../pages/AboutMe">
					<h1>About Me</h1>
				</Link>
			</div>
		</header>
	)
};

export default AboutMeToolbar;