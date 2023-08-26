// Toolbar to be used for navigation purposes of the website
import { Link } from 'react-router-dom'

const TopToolbar = () => {
	return (
		<header>
			<div className="container1">
				<Link to="/">
					<h1>Movie Recommendation System</h1>
				</Link>
			</div>
		</header>
	)
};

export default TopToolbar;