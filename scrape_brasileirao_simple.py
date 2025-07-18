#!/usr/bin/env python3
"""
Brazilian Soccer Championship 2025 Classification Scraper
Compares actual standings with player predictions and calculates scores.
"""

import json
import os
import urllib.request
import urllib.parse
import ssl
import re
from datetime import datetime

class BrasileiroScraper:
    def __init__(self):
        # Create SSL context that doesn't verify certificates (for testing)
        self.ssl_context = ssl.create_default_context()
        self.ssl_context.check_hostname = False
        self.ssl_context.verify_mode = ssl.CERT_NONE
        
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    
    def load_predictions(self, json_file="bolao.json"):
        """Load player predictions from JSON file"""
        try:
            if not os.path.exists(json_file):
                print(f"Predictions file not found: {json_file}")
                return None
            
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            return data
        except Exception as e:
            print(f"Error loading predictions: {e}")
            return None
    
    def fetch_url(self, url):
        """Fetch URL content"""
        try:
            req = urllib.request.Request(url, headers=self.headers)
            with urllib.request.urlopen(req, context=self.ssl_context) as response:
                return response.read().decode('utf-8')
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None
    
    def scrape_espn_standings(self):
        """Scrape standings from ESPN Brazil"""
        url = "https://www.espn.com.br/futebol/liga/_/nome/bra.1"
        
        print("Fetching standings from ESPN Brazil...")
        html_content = self.fetch_url(url)
        
        if not html_content:
            return None
        
        # Parse the HTML to extract standings
        teams = []
        
        # Look for table rows with team data using regex
        # This is a simplified approach - finding table rows
        table_pattern = r'<tr[^>]*>.*?</tr>'
        rows = re.findall(table_pattern, html_content, re.DOTALL | re.IGNORECASE)
        
        position = 1
        for row in rows:
            # Skip header rows
            if 'th>' in row or 'header' in row.lower():
                continue
            
            # Look for team names - ESPN typically has team names in links or specific classes
            team_match = re.search(r'<a[^>]*>([^<]*(?:Flamengo|Palmeiras|São Paulo|Corinthians|Grêmio|Internacional|Atlético|Santos|Fluminense|Botafogo|Vasco|Bahia|Cruzeiro|Fortaleza|Ceará|Sport|Vitória|Athletico|Bragantino|Juventude|Mirassol|Cuiabá|Goiás|Coritiba|América)[^<]*)</a>', row, re.IGNORECASE)
            
            if team_match:
                team_name = team_match.group(1).strip()
                # Clean up team name
                team_name = re.sub(r'\s+', ' ', team_name)
                
                # Extract points/stats from the row
                cells = re.findall(r'<td[^>]*>(.*?)</td>', row, re.DOTALL | re.IGNORECASE)
                
                if len(cells) >= 5:  # Minimum columns expected
                    # Clean cell content
                    clean_cells = []
                    for cell in cells:
                        clean_text = re.sub(r'<[^>]+>', '', cell).strip()
                        clean_cells.append(clean_text)
                    
                    teams.append({
                        'position': position,
                        'team': team_name,
                        'points': clean_cells[-1] if clean_cells else '0',  # Points usually last column
                        'games': clean_cells[1] if len(clean_cells) > 1 else '0'
                    })
                    position += 1
                    
                    if position > 20:  # Brasileirão has 20 teams
                        break
        
        return teams if teams else None
    
    def scrape_ge_globo_standings(self):
        """Scrape standings from GE Globo"""
        url = "https://ge.globo.com/futebol/brasileirao-serie-a/"
        
        print("Fetching standings from GE Globo...")
        html_content = self.fetch_url(url)
        
        if not html_content:
            return None
        
        teams = []
        
        # Look for classification table
        table_pattern = r'<table[^>]*class="[^"]*classificacao[^"]*"[^>]*>(.*?)</table>'
        table_match = re.search(table_pattern, html_content, re.DOTALL | re.IGNORECASE)
        
        if table_match:
            table_content = table_match.group(1)
            rows = re.findall(r'<tr[^>]*>(.*?)</tr>', table_content, re.DOTALL | re.IGNORECASE)
            
            position = 1
            for row in rows:
                # Skip header
                if 'th>' in row:
                    continue
                
                # Look for team names
                team_match = re.search(r'<td[^>]*>.*?([A-Za-z\s]+(?:Flamengo|Palmeiras|São Paulo|Corinthians|Grêmio|Internacional|Atlético|Santos|Fluminense|Botafogo|Vasco|Bahia|Cruzeiro|Fortaleza|Ceará|Sport|Vitória|Athletico|Bragantino|Juventude|Mirassol)[A-Za-z\s]*)', row, re.IGNORECASE)
                
                if team_match:
                    team_name = team_match.group(1).strip()
                    
                    # Extract cell data
                    cells = re.findall(r'<td[^>]*>(.*?)</td>', row, re.DOTALL | re.IGNORECASE)
                    clean_cells = []
                    for cell in cells:
                        clean_text = re.sub(r'<[^>]+>', '', cell).strip()
                        clean_cells.append(clean_text)
                    
                    if clean_cells:
                        teams.append({
                            'position': position,
                            'team': team_name,
                            'points': clean_cells[2] if len(clean_cells) > 2 else '0',
                            'games': clean_cells[1] if len(clean_cells) > 1 else '0'
                        })
                        position += 1
                        
                        if position > 20:
                            break
        
        return teams if teams else None
    
    def get_current_standings(self):
        """Get current standings by scraping from online sources"""
        print("Scraping current Brazilian Championship 2025 standings...")
        
        # Try multiple sources
        sources = [
            ("ESPN Brazil", self.scrape_espn_standings),
            ("GE Globo", self.scrape_ge_globo_standings)
        ]
        
        for source_name, scraper_func in sources:
            try:
                standings = scraper_func()
                if standings and len(standings) >= 15:  # At least 15 teams found
                    print(f"✅ Successfully scraped {len(standings)} teams from {source_name}")
                    return standings
                else:
                    print(f"❌ {source_name}: Insufficient data ({len(standings) if standings else 0} teams)")
            except Exception as e:
                print(f"❌ {source_name}: Error - {e}")
        
        # No fallback - if scraping fails, return None
        print("❌ All scraping sources failed")
        return None
    
    def normalize_team_name(self, team_name):
        """Normalize team names to match predictions"""
        # Clean up the team name
        team_name = team_name.strip()
        
        # Handle common variations
        name_mappings = {
            'Red Bull Bragantino': 'Bragantino',
            'RB Bragantino': 'Bragantino',
            'Vasco da Gama': 'Vasco',
            'Atlético-MG': 'Atlético-MG',
            'Atlético Mineiro': 'Atlético-MG',
            'Athletico-PR': 'Athletico-PR',
            'Athletico Paranaense': 'Athletico-PR',
            'Red Bull Salzburg': 'Bragantino',  # Just in case
        }
        
        # Check direct mappings
        if team_name in name_mappings:
            return name_mappings[team_name]
        
        # Check if any mapping key contains the team name or vice versa
        for key, value in name_mappings.items():
            if key.lower() in team_name.lower() or team_name.lower() in key.lower():
                return value
        
        return team_name
    
    def calculate_score(self, predicted_pos, actual_pos):
        """Calculate score: 20 points minus absolute deviation"""
        deviation = abs(predicted_pos - actual_pos)
        score = max(0, 20 - deviation)  # Minimum score is 0
        return score
    
    def compare_predictions(self, actual_standings, predictions):
        """Compare predictions with actual standings and calculate scores"""
        if not predictions or not actual_standings:
            return
        
        # Calculate scores for each player
        player_scores = {}
        
        print(f"\n🏆 BRASILEIRÃO 2025 - BOLÃO RESULTS")
        print(f"Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 120)
        
        # Header
        print(f"{'Team':<20} {'Actual':<8}", end="")
        for player in predictions.keys():
            print(f"{player:<12}", end="")
        print()
        print("-" * 120)
        
        # Process each team
        for team_data in actual_standings:
            original_team_name = team_data['team']
            team_name = self.normalize_team_name(original_team_name)
            actual_pos = team_data['position']
            
            print(f"{original_team_name:<20} {actual_pos:<8}", end="")
            
            for player, player_predictions in predictions.items():
                if player not in player_scores:
                    player_scores[player] = 0
                
                # Find predicted position for this team
                predicted_pos = None
                for pos, predicted_team in player_predictions.items():
                    if predicted_team == team_name:
                        predicted_pos = int(pos)
                        break
                
                if predicted_pos is not None:
                    score = self.calculate_score(predicted_pos, actual_pos)
                    player_scores[player] += score
                    print(f"{predicted_pos}°({score}p) ", end="")
                else:
                    print("--       ", end="")
            
            print()
        
        # Display final scores
        print("-" * 120)
        print(f"{'FINAL SCORES:':<20} {'':>8}", end="")
        for player in predictions.keys():
            print(f"{player_scores.get(player, 0):<12}", end="")
        print()
        
        # Ranking
        print(f"\n🏅 RANKING:")
        sorted_players = sorted(player_scores.items(), key=lambda x: x[1], reverse=True)
        for i, (player, score) in enumerate(sorted_players, 1):
            print(f"{i}. {player}: {score} points")
        
        return player_scores
    
    def update_readme(self, actual_standings, predictions, player_scores):
        """Update README.md with the latest results"""
        try:
            # Sort players by score (highest first)
            sorted_players = sorted(player_scores.items(), key=lambda x: x[1], reverse=True)
            player_names = [player[0] for player in sorted_players]
            
            # Generate the results table
            results_table = []
            results_table.append("## 🏆 Resultados Atuais")
            results_table.append("")
            results_table.append(f"**Última Atualização:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            results_table.append("")
            
            # Create table header with players sorted by score
            header = "| Time | Real |"
            for player in player_names:
                header += f" {player} |"
            results_table.append(header)
            
            # Create separator
            separator = "|------|------|"
            for _ in player_names:
                separator += "------|"
            results_table.append(separator)
            
            # Create rows for each team
            for team_data in actual_standings:
                original_team_name = team_data['team']
                team_name = self.normalize_team_name(original_team_name)
                actual_pos = team_data['position']
                
                row = f"| {original_team_name} | {actual_pos} |"
                
                for player in player_names:
                    player_predictions = predictions[player]
                    # Find predicted position for this team
                    predicted_pos = None
                    for pos, predicted_team in player_predictions.items():
                        if predicted_team == team_name:
                            predicted_pos = int(pos)
                            break
                    
                    if predicted_pos is not None:
                        score = self.calculate_score(predicted_pos, actual_pos)
                        row += f" {predicted_pos}°({score}p) |"
                    else:
                        row += " -- |"
                
                results_table.append(row)
            
            # Add total scores row
            total_row = "| **TOTAL** | |"
            for player in player_names:
                total_row += f" **{player_scores[player]}** |"
            results_table.append(total_row)
            
            # Add ranking
            results_table.append("")
            results_table.append("### 🏅 Classificação Final")
            results_table.append("")
            for i, (player, score) in enumerate(sorted_players, 1):
                medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"{i}."
                results_table.append(f"{medal} **{player}**: {score} pontos")
            
            # Read current README
            readme_path = "README.md"
            if os.path.exists(readme_path):
                with open(readme_path, 'r', encoding='utf-8') as f:
                    readme_content = f.read()
                
                # Find and replace the results section
                results_section = "\n".join(results_table)
                
                # Check if results section exists
                if "## 🏆 Resultados Atuais" in readme_content:
                    # Replace existing results section - match everything from results until next ## or end
                    import re
                    pattern = r'## 🏆 Resultados Atuais.*?(?=\n## |\Z)'
                    new_content = re.sub(pattern, results_section, readme_content, flags=re.DOTALL)
                else:
                    # Add results section at the beginning after the title
                    lines = readme_content.split('\n')
                    title_line = 0
                    for i, line in enumerate(lines):
                        if line.startswith('# '):
                            title_line = i
                            break
                    
                    # Insert results after title
                    lines.insert(title_line + 1, '')
                    lines.insert(title_line + 2, results_section)
                    new_content = '\n'.join(lines)
                
                # Write back to README
                with open(readme_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print(f"✅ Updated README.md with latest results")
                
            else:
                print("❌ README.md not found")
                
        except Exception as e:
            print(f"❌ Error updating README: {e}")
    
    def run_comparison(self, predictions_file="bolao.json"):
        """Main method to run the comparison"""
        try:
            # Get current standings
            current_standings = self.get_current_standings()
            
            # Load predictions
            predictions = self.load_predictions(predictions_file)
            
            if current_standings and predictions:
                # Compare and calculate scores
                scores = self.compare_predictions(current_standings, predictions)
                
                # Update README with results
                self.update_readme(current_standings, predictions, scores)
                
                print(f"\n✅ Successfully compared {len(current_standings)} teams")
                print(f"✅ Calculated scores for {len(predictions)} players")
            else:
                print("❌ Failed to load data")
                
        except Exception as e:
            print(f"❌ Error: {e}")

def main():
    scraper = BrasileiroScraper()
    
    # Check if predictions file is provided as argument
    import sys
    predictions_file = sys.argv[1] if len(sys.argv) > 1 else "bolao.json"
    
    scraper.run_comparison(predictions_file)

if __name__ == "__main__":
    main()
